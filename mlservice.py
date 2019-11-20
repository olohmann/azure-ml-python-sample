import azureml.core
import os
from azureml.core import authentication
from azureml.core import Workspace
from dotenv import load_dotenv

def configure_workspace():
    auth = authentication.InteractiveLoginAuthentication()

    SUBSCRIPTION_ID = os.getenv('SUBSCRIPTION_ID')
    RESOURCE_GROUP_NAME = os.getenv('RESOURCE_GROUP_NAME')
    WORKSPACE_NAME = os.getenv('WORKSPACE_NAME')
    REGION = os.getenv('REGION')

    ws = None
    try:
        # Find existing workspace
        ws = Workspace(workspace_name=WORKSPACE_NAME,
                    subscription_id=SUBSCRIPTION_ID,
                    resource_group= RESOURCE_GROUP_NAME,
                    auth=auth)
        print (ws.name, "found.")
    except Exception as ex:
        # If workspace not found, create it
        print(ex.message)
        print("Attempting to create new workspace...")
        ws = Workspace.create(name=WORKSPACE_NAME, 
                        subscription_id=SUBSCRIPTION_ID,
                        resource_group=RESOURCE_GROUP_NAME,
                        create_resource_group=True,
                        location=REGION,
                        auth=auth)
        print(ws.name, "created.")
    finally:
        # Save the workspace configuration for later
        if ws != None:
            ws.write_config()
            print(ws.name, "saved.")

    #Check if config was created
    with open("./.azureml/config.json","r") as f:
        print(f.read())

    ws = Workspace.from_config()
    print(ws.name, "loaded")
    return ws

def main():
    load_dotenv()
    ws = configure_workspace()

if __name__ == "__main__":
    main()
