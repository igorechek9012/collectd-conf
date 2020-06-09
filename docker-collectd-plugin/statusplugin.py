import collectd
import docker

containerStatus = {
	'restarting': 3,
	'running': 1,
	'paused': 2,
	'exited': 0
}

def read(data=None):
        client = docker.DockerClient(base_url='unix://var/run/docker.sock')
	containers = client.containers.list(all=True)
	containersData = []
	for container in containers:
		containersData.append({
			'id': container.id,
			'name': container.name,
			'status': container.status,
			'statusId': containerStatus[container.status]	
		})
	for data in containersData:
		vl = collectd.Values(type='container_status')
	    	vl.plugin='docker_status'
		vl.plugin_instance = data['name']
	    	vl.dispatch(values=[data['statusId']])
			

collectd.register_read(read)

