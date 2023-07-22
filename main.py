from sklearn.neighbors import NearestNeighbors
import cherrypy


class LogisticsAPI(object):
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def index(self):
        data = cherrypy.request.json
        package_locations = data.get('package_locations')
        driver_locations = data.get('driver_locations')

        # Create a nearest neighbor model
        neighbors = NearestNeighbors(n_neighbors=1)
        neighbors.fit(driver_locations)

        # Find the nearest driver for each package
        distances, indices = neighbors.kneighbors(package_locations)

        # output
        string_list = []

        # Print out the assignments
        for package_idx, driver_idx in enumerate(indices):
            string_list.append(f"Package {package_idx + 1} is assigned to driver {driver_idx[0] + 1}")

        # Here you'd use your assignment logic
        # For simplicity, let's just return the received data
        return {'result': string_list}


if __name__ == '__main__':
    config = {'server.socket_host': '0.0.0.0'}
    cherrypy.config.update(config)
    cherrypy.quickstart(LogisticsAPI(), '/')
