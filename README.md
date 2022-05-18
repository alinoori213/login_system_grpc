## Django gRPC authentication service
___

#### STEP 1: Install packages
```pip install -r requirements.txt```
#### STEP 2: Make migrations and migrate
```python
python manage.py makemigrations
python manage.py migrate
```
#### STEP 3: Generate proto files
```python 
python manage.py generateproto --model users.models.CustomUser  --file proto/user/user.proto
```

#### STEP 4: Generate gRPC code
```python 
python -m grpc_tools.protoc -I ./  --python_out=./ --grpc_python_out=./ ./proto/auth.proto
python -m grpc_tools.protoc -I ./  --python_out=./ --grpc_python_out=./ ./proto/user.proto
```

#### STEP 5: Run server
```python
python manage.py grpcrunserver
```
