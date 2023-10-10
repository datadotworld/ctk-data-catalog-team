import os
import random
import sys

def create_directory_and_files(private_instance, prefix=None):
    # Create directory
    # os.mkdir(dir_name)

    # List of file names
    # As long as prefix is provided, it should be added to file name
    if prefix != None:
        file_names = [
            f"cc_variables_{private_instance}-{prefix}-data-catalog-team.properties"
        ]

        # List of random texts
        data_catalog_team = [
            f"privateInstance = {private_instance}\n",
            f"dataCatalogTeamIdentifier = {prefix}-data-catalog-team"
        ]
    else:
        file_names = [
            f"cc_variables_{private_instance}-data-catalog-team.properties"
            ]

        # List of random texts
        data_catalog_team = [
            f"privateInstance = {private_instance}\n",
            f"dataCatalogTeamIdentifier = data-catalog-team"
        ]

    # Create and write to each file
    for file_name in file_names:
        if "data-catalog-team" in file_name:
            with open(f"template/customer_config/{file_name}", "w") as file:
                for line in data_catalog_team:
                    file.write(line)
        else:
            pass

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("This script creates Catalog Config related .properties files\nWhen the CTK orgs have a slug such as `training-catalog-config` provide the slug e.g.\n python3 script.py <private_instance> <slug>\nIf the CTK orgs do not have a slug, the usage is\n python3 script.py <private_instance>")
        # sys.exit(1)
    
    if len(sys.argv) == 2:
        ## when the CTK orgs agentIDs are `catalog-config` and `catalog-sources`, set the PI name as the prefix
        private_instance = sys.argv[1]
        prefix = None
        print(f'Creating {private_instance}- .properties files.')
    elif len(sys.argv) == 3:
        ## when the CTK orgs agentID has a slug e.g. `training-catalog-config` and `training-catalog-sources`, provide 
        private_instance = sys.argv[1]
        prefix = sys.argv[2]
        print(f'Creating {private_instance}-{prefix}- .properties files.')
    else:
        print("Please provide at least one arguments for private instance name if prefix does not present!")
    create_directory_and_files(private_instance, prefix)