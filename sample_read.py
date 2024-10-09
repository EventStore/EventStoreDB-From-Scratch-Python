from esdbclient import EventStoreDBClient, NewEvent, StreamState

client = EventStoreDBClient(uri="esdb://localhost:2113?tls=false")

events = client.get_stream("SampleStream")

for event in events:
    print("************************");
    print("You have read an event!");
    print("Stream: " + event.stream_name);
    print("Event Type: " + event.type);
    print("Event Body: " + event.data.decode());
    print("************************");

client.close()