import dialogflow_v2beta1
client=dialogflow_v2beta1.AgentsClient()
parent=client.project_path('[PROJECT]')
client.delete_agent(parent)