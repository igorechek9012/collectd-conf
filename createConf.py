import os
from sys import argv

createPluginDirCmd = 'sudo mkdir /home/igor/distrub'
copyPluginCmd = 'sudo cp -R ./docker-collectd-plugin /home/igor/distrub/docker-collectd-plugin'
copyPluginConfCmd1 = 'sudo cp ./conf/docker-plugin.conf /etc/collectd/conf'
copyPluginConfCmd2 = 'sudo cp ./conf/statusplugin.conf /etc/collectd/conf'
copyScriptCmd = 'sudo cp collectd.conf /etc/collectd/'
restartCollectdCmd = 'sudo systemctl restart collectd'
hostName = argv[1]
hostNameString = 'Hostname "' + hostName + '"\n'
with open('collectd.conf', 'w') as outfile:
	outfile.write(hostNameString)
        with open('collectd-def.conf') as infile:
            outfile.write(infile.read())
os.system (createPluginDirCmd)
os.system (copyPluginCmd)
os.system (copyPluginConfCmd1)
os.system (copyPluginConfCmd2)
os.system (copyScriptCmd)
os.system (restartCollectdCmd)
print("End")




