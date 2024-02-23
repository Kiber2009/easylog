# easylog
## About
easylog is a simple python logging library
## Usage example
```python
import easylog

logger = easylog.Logger('last.log')

logger.info('Info here')
logger.warn('Warn here')
logger.error('Error here')

logger.custom('Custom type', 'Custom here')
```
## Installing
```shell
pip install easylog
```
## Building from source code
* Clone the repo
  ```shell
  git clone https://github.com/Kiber2009/easylog.git
  cd easylog
  ```
* Make sure you have the latest version of PyPA’s build installed
  ```shell
  py -m pip install --upgrade build
  ```
* Build the lib
  ```shell
  py -m build
  ```