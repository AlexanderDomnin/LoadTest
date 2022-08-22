from locust import between, events, tag, task, HttpUser, TaskSet, HttpLocust

from locust_influxdb_listener import InfluxDBListener, InfluxDBSettings
from core.api import Headers, Params


def login(l):
    response = l.client.post(
        "/api/v1/security/login",
        json={
            "password": "1",
            "provider": "db",
            "refresh": True,
            "username": "admin"
        }
    )

    return response.json()['access_token']

#@events.init.add_listener
#def on_locust_init(environment, **_kwargs):
#    """
#    Hook event that enables starting an influxdb connection
#    """
#    # this settings matches the given docker-compose file
#    influxDBSettings = InfluxDBSettings(
#        influx_host='localhost',
#        influx_port='8086',
#        user='admin',
#        pwd='pass',
#        database='test-project'
#    )
    # start listerner with the given configuration
#    InfluxDBListener(env=environment, influxDbSettings=influxDBSettings)

class QuickstartUser(HttpUser):
    def on_start(self):
        token = login(self)
        return token

    @tag('home_page')
    @task
    def home_page(self):
        with self.client.get("/", catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Got wrong response")

    @tag('get_dashboard')
    @task(1)
    def get_dashboard(self, token=on_start()):
        self.client.get(
                url="/api/v1/dashboard",
                params=Params.PARAMS_GET_DASHBOARD,
                headers=Headers.AUTHORIZATION(token)
        )

    @tag('add_dashboard')
    @task(2)
    def add_dashboard(self):
        self.client.post(
            url="/api/v1/dashboard",
            params=Params.PARAMS_GET_DASHBOARD,
            headers=Headers.TOKEN,
            data={"certification_details": "",
                    "certified_by": "",
                    "css": "",
                    "dashboard_title": "Test1235",
                    "json_metadata": "{\"show_native_filters\":true,\"color_scheme\":\"\",\"positions\":{\"DASHBOARD_VERSION_KEY\":\"v2\",\"ROOT_ID\":{\"type\":\"ROOT\",\"id\":\"ROOT_ID\",\"children\":[\"GRID_ID\"]},\"GRID_ID\":{\"type\":\"GRID\",\"id\":\"GRID_ID\",\"children\":[\"TABS-cjyBly45qY\"],\"parents\":[\"ROOT_ID\"]},\"HEADER_ID\":{\"id\":\"HEADER_ID\",\"type\":\"HEADER\",\"meta\":{\"text\":\"Test123\"}},\"TABS-cjyBly45qY\":{\"type\":\"TABS\",\"id\":\"TABS-cjyBly45qY\",\"children\":[\"TAB-aw_3vmbrAr\"],\"parents\":[\"ROOT_ID\",\"GRID_ID\"],\"meta\":{}},\"TAB-aw_3vmbrAr\":{\"type\":\"TAB\",\"id\":\"TAB-aw_3vmbrAr\",\"children\":[],\"parents\":[\"ROOT_ID\",\"GRID_ID\",\"TABS-cjyBly45qY\"],\"meta\":{\"text\":\"\",\"defaultText\":\"Tab title\",\"placeholder\":\"Tab title\"}}},\"refresh_frequency\":0,\"shared_label_colors\":{},\"expanded_slices\":{},\"label_colors\":{},\"timed_refresh_immune_slices\":[],\"default_filters\":\"{}\",\"filter_scopes\":{},\"chart_configuration\":{}}",
                    "owners": [1],
                    "slug": None},
        ),



