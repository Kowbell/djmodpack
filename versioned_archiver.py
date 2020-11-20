import os
import subprocess

# Forward declared key variables
versionStr = ""
versionMajor = -1
versionMinor = -1

# Get version number
with open('currentVersion.txt', 'r') as versionFile:
	lineVersions = versionFile.readline().split('.')
	versionMajor = int(lineVersions[0])
	versionMinor = int(lineVersions[1])


# Increment version
versionMinor += 1
versionStr = "{}.{}".format(versionMajor, versionMinor)
print("Version {}".format(versionStr))

# Do the zip
command = [
	'7z', # Use 7z command utility...
	'a',  # ... to make a new archive...
	'djmodpack-release/djmodpack-{}.zip'.format(versionStr), 
	#       ... call that archive "djmodpack-x.y.zip'
	#           and put it in the release dir...
	'./djmodpack-src/*'
	#       ... and use the contents of the src dir
	#           to populate the archive. The zip will
	#           contain whatever's in the src folder
	#           WITHOUT having the src folder as the
	#           first thing you see when you open!
	]

print("==============================")
proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = proc.communicate()
stdout_str = stdout.decode("utf-8")
print(stdout_str)
print("==============================")

if not stdout_str.endswith("Everything is Ok\n"):
	print("ERROR ARCHIVING! STDERR=")
	print(str(stderr))
	exit(1)

print("Done packaging version {} for release!".format(versionStr))

# Save version
with open('currentVersion.txt', 'w') as versionFile:
	versionFile.write(versionStr)