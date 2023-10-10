import sys

# Print usage if arguments are missing
if len(sys.argv) < 2:
    print(f"Usage: python CreateCircleCIJob.py private_instance [prefix]")
    print(f"\nCreates a CircleCI job to deploy a private instance with the given private_instance name and optional prefix.")
    sys.exit(1)

private_instance = sys.argv[1]
prefix = sys.argv[2] if len(sys.argv) > 2 else ""

slug = private_instance if not prefix else f"{private_instance}-{prefix}"

# Create the CircleCI job text using f-strings
text = f"""
  deploy_privateinstance_catalog_config_{slug}:
    <<: *dwt_setup
    steps:
      - run:
          command: |
            echo CUSTOMER_CATALOG_CONFIG="{slug}-data-catalog-team" >> ~/.env
            echo PRIVATE_INSTANCE_CUSTOMER_API_URL=api.data.world >> ~/.env
            echo CUSTOMER_API_TOKEN=${private_instance.upper()}_API_TOKEN >> ~/.env
      - preprocessing_python_scripts
      - run_commands_data_catalog_team_deploy
"""

print(text)