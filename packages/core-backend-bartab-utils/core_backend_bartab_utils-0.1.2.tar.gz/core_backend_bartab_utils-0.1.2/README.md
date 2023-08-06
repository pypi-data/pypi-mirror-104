# Core Utils Python

_Updated Wednesday May 5th 2021 by [cassioblu55](https://github.com/cassioblu55)_

Common python code for BarTab python repositories. Hosted in pip production [here](https://pypi.org/project/core-backend-bartab-utils/), test pip hosted [here](https://test.pypi.org/project/core-backend-bartab-utils/)


## Manual Release
In order to release a new version run the following:
```bash 
python setup.py sdist
```

## External References
How to create a pip package is walked through [here](https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python-pypi-packaging/)

## Features

1. **Issue Templates**
   1. _Bug Report_ - Create a bug report issue
   2. _Feature Request_ - Create feature request/enhancement
   3. _Dev Ops Request_ - Create a new development operations request, this can be sever management, user access item, workflow automation enhancement, or a report of issues going on with cloud infrastructure
   4. _Test Request_ - Create test automation or manual testing request
2. **Workflows**
   1. _Auto Assign Issues and PRs to Main Org Project_ - Will link new issues and pull requests to: [Master Bartab Project](https://github.com/orgs/BarTabPayments/projects/3)
   2. _Auto Assign Issues and PRs to Main Repo Project_ - Will link new issues and pull requests to project within this repo
   3. _Auto Assign_ - Using [Auto Assign](https://github.com/apps/auto-assign) will assign the creator of a pull request to the author of the pull request
