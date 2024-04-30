from esdbclient import EventStoreDBClient, NewEvent, StreamState

client = EventStoreDBClient(uri="esdb://localhost:2113?tls=false")



events = client.get_stream("SampleContent")

for event in events:
    print(event.data)

print("success")
client.close()


