from esdbclient import EventStoreDBClient, NewEvent, StreamState    # Import the necessary modules from the esdbclient package

#######################################################
#
# Step 1. Create client and connect it to EventStoreDB
#
#######################################################

# Create an instance of EventStoreDBClient, connecting to the EventStoreDB at localhost without TLS
client = EventStoreDBClient(uri="esdb://localhost:2113?tls=false")

################################################
#
# Step 2. Read all events from the SampleStream
#
################################################

events = client.get_stream("SampleStream")  # Read all events from SampleStream

######################################
#
# Step 3. Print each event to console
#
######################################

for event in events:
    print("************************");
    print("You have read an event!");
    print("Stream: " + event.stream_name);
    print("Event Type: " + event.type);
    print("Event Body: " + event.data.decode());
    print("************************");

client.close()