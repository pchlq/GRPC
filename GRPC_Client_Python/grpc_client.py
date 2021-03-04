import grpc
import greeting_service_pb2
import greeting_service_pb2_grpc

# python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. greeting_service.proto

def run():
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = greeting_service_pb2_grpc.GreetingServiceStub(channel)

        # for single response
        # response = stub.greeting(greeting_service_pb2.HelloRequest(name='Pavel'))

        # for stream
        for response in stub.greeting(greeting_service_pb2.HelloRequest(name='Pavel')):
            print("Greeting from Server: " + response.greeting)

run()