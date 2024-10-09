from esdbclient import EventStoreDBClient, NewEvent, StreamState

client = EventStoreDBClient(uri="esdb://localhost:2113?tls=false")

event_type = "SampleEvent"
new_event = NewEvent(
    type="SampleEvent",
    data=b'{"Id":"1", "importantData":"some value"}'
)

event_stream = "SampleStream"
client.append_to_stream(
    "SampleStream",
    events = [new_event],
    current_version = StreamState.ANY
)

print("************************");
print("🎉 Congratulations, you have written an event!");
print("Stream: " + event_stream);
print("Event Type: " + event_type);
print("Event Body: " + new_event.data);
print("************************");

client.close()