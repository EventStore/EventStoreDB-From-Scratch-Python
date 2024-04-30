from esdbclient import EventStoreDBClient, NewEvent, StreamState

client = EventStoreDBClient(uri="esdb://localhost:2113?tls=false")

new_event = NewEvent(
    type="some-event",
    data=b'{"Id":"1", "value":"some data"}'
)

client.append_to_stream(
    "SampleContent",
    events = [new_event],
    current_version = StreamState.ANY
)
client.close()

