import os
import pandas
from google.cloud import dialogflow_v2beta1 as dialogflow

# Set credential file path here
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./test-key.json"

# vars for writing to excel file
fileName = 'intents.xlsx'
allRows = []


def process_response(line):
    # string processing for response to copy paste into synthesia easier
    line = str(line)
    line = line[7:-2]
    line = line.replace('\\', '')
    line = line.replace('&', 'and')
    line = line.replace('\"', '')
    line += "<break time=\"2s\" />"
    return line


def process_intent_name(line):
    # string processing for intent name to make into suitable file name
    line = line.replace('\\', '')
    line = line.replace('/', '')
    line = line.replace('&', 'and')
    line = line.replace('\'', '')
    line = line.replace('\"', '')
    line = line.replace(' ', '_')
    return line


def write_intent_name_to_text_file(line):
    with open('videoName.txt', 'a') as f:
        f.write(line)
        f.write('\n')


def get_intents(project_id):
    # get intents from dialogflow
    intents_client = dialogflow.IntentsClient()
    parent = dialogflow.AgentsClient.agent_path(project_id)
    intents = intents_client.list_intents(request={"parent": parent})
    

    # for storing [0] intent display name & [1] corresponding intent response
    individualRow = []

    for intent in intents:
        # clear individual row at beginning
        individualRow = []

        print('Intent display_name: {}'.format(intent.display_name))
        print("Intent responses: ")
        print(intent.messages)

        if (len(intent.messages) > 0):
            # put intent names in a txt file
            processedIntentName = process_intent_name(intent.display_name)
            write_intent_name_to_text_file(processedIntentName)

            # add intent name and response to row
            individualRow.append(processedIntentName)
            individualRow.append(process_response(intent.messages[0].text))

        # add row to entire "excel sheet"
        allRows.append(individualRow)

def print_intents(project_id):
    #FROM https://cloud.google.com/dialogflow/es/docs/how/manage-intents#list-intents
    intents_client = dialogflow.IntentsClient()
    parent = dialogflow.AgentsClient.agent_path(project_id)
    intents = intents_client.list_intents(request={"parent": parent})

    for intent in intents:
        print("=" * 20)
        print("Intent name: {}".format(intent.name))
        print("Intent display_name: {}".format(intent.display_name))
        print("Action: {}\n".format(intent.action))
        print("Root followup intent: {}".format(intent.root_followup_intent_name))
        print("Parent followup intent: {}\n".format(intent.parent_followup_intent_name))

        print("Input contexts:")
        for input_context_name in intent.input_context_names:
            print("\tName: {}".format(input_context_name))

        print("Output contexts:")
        for output_context in intent.output_contexts:
            print("\tName: {}".format(output_context.name))
    

# Set your project id here
get_intents("shreya-epr9")

# write to excel file
df = pandas.DataFrame(allRows)
df.to_excel(fileName, index=False, header=False)
