import common
import os               # for env vars
from shutil import copy	# file manipulation

env = common.prepare_env()

# set tag to app_version.txt
if not env["GITHUB_TAG"] == "":
  with open("./resources/app/meta/manifests/app_version.txt","w+") as f:
	  _ = f.read()
	  f.seek(0)
	  f.write(env["GITHUB_TAG"])
	  f.truncate()

if not os.path.isdir("../build"):
	os.mkdir("../build")
copy(
	"./resources/app/meta/manifests/app_version.txt",
	"../build/app_version.txt"
)
