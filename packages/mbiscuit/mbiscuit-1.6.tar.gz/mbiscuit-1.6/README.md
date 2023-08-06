生成依赖文件

```bash
pip freeze >requirements.txt
```` 

根据依赖文件安装依赖

```bash
pip install -r requirements.txt -i http://192.168.7.78:8084/repository/group-pypi/simple  --trusted-host 192.168.7.78 
````

pip更换源

```bash
pip install mbiscuit -i http://192.168.7.78:8084/repository/group-pypi/simple  --trusted-host 192.168.7.78 

````

打包

```bash
python setup.py sdist bdist_wheel

````

上传

```bash
twine upload -r nexus dist/mbiscuit-1.1.tar.gz --repository-url=http://192.168.7.78:8084/repository/pypi/

````

上传pypi

```bash
twine upload dist/mbiscuit-1.5.tar.gz 

````