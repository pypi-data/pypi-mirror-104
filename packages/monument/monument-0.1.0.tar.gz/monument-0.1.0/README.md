This is a python interface to Monument model serving.

## Requirements

* Monument gui version 1.14 or later

* python 3 with numpy (tested with python 3.8)

## How to Use

### Import

```
from monument import monument
```

### Initialize

Initialize with the installation directory of Monument app on your machine.

On Windows or Mac, the directory can be omitted,

```
monument.init("")
```

On Linux, look from your home directory.

```
from os.path import expanduser
home = expanduser("~").replace("\\","/")
monument.init(home + "/MonumentDev")
```

### Serve

Specify the location of your maifile (`.mai`), serving data file (`.csv`), and algo name (`ALGO(COLUMN)`).

The algo name must match the model in the maifile.

```
maifile = "tests/data/insure.mai"
csvfile = "tests/data/insure2.csv"
algo = "Ent-Boost(AIG)"
res = monument.serve(maifile,csvfile,algo)
print(res)
```
