from esdbclient import EventStoreDBClient, NewEvent, StreamState    # Import the necessary modules from the esdbclient package

#######################################################
#
# Step 1. Create client and connect it to EventStoreDB
#
#######################################################


#########################
# Create an instance of EventStoreDBClient, 
# connecting to the EventStoreDB at localhost without TLS
# To run against another instance of KurrentDB or a 
# KurrentDB cloud cluster.
# Replace this line with the connection string to your cluster
# 
###########
# client = EventStoreDBClient(uri="esdb://localhost:2113?tls=false") 
client = EventStoreDBClient("esdb+discover://admin:6906b7791d76454bb4fae6faf590ab06@kurrentdb.curr4icgdub1aodg1sh0.cui3cs4gduba0bunfq60.sites.platform.eventstore.cloud:2113") 



############################################################
#
# Step 2. Create new event object with a type and data body
#
############################################################

event_type = "SampleEventType"                        # Define the event type for the new event
new_event = NewEvent(                                 # Create a new event with a type and body
    type=event_type,                                  # Specify the event type
    data=b'{"id":"1", "importantData":"some value"}'  # Specify the event data body as a JSON in byte format
)

##################################################
#
# Step 3. Append the event object into the stream
#
##################################################

event_stream = "SampleStream"        # Define the stream name where the event will be appended
client.append_to_stream(             # Append the event to a stream
    event_stream,                    # Name of the stream to append the event to
    events=[new_event],              # The event to append (in a list)
    current_version=StreamState.ANY  # Set to append regardless of the current stream state (you can ignore this for now)
)

##############################################
#
# Step 4. Print the appended event to console
#
##############################################

print("************************") 
print("🎉 Congratulations, you have written an event!") 
print("Stream: " + event_stream) 
print("Event Type: " + event_type) 
print("Event Body: " + new_event.data.decode()) 
print("************************") 

client.close()  # Close the connection to EventStoreDB