import yaml

# Load the groups YAML file
with open('info.yml', 'r') as file:
    groups_data = yaml.safe_load(file)

# Extract the group names
group_names = list(groups_data.get('groups', {}).keys())

# Save the extracted group names in a new YAML file
with open('groups.yml', 'w') as file:
    yaml.dump({'group_names': group_names}, file)
