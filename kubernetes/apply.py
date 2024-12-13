import subprocess

def apply_kubectl_command(command):
    """Function to run kubectl apply commands."""
    try:
        # Run the kubectl apply command
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Success: {command}")
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error applying command: {command}")
        print(e.stderr.decode())

def main():
    # List of kubectl apply commands with paths to your YAML files
    commands = [
        "kubectl apply -f ./kubernetes/alertmanager-service.yml",
        "kubectl apply -f ./kubernetes/deployment.yml",
        "kubectl apply -f ./kubernetes/prometheus-clusterrole.yml",
        "kubectl apply -f ./kubernetes/prometheus-clusterrolebinding.yml",
        "kubectl apply -f ./kubernetes/prometheus-config.yml",
        "kubectl apply -f ./kubernetes/prometheus-deployment.yml",
        "kubectl apply -f ./kubernetes/prometheus-rules.yml",
        "kubectl apply -f ./kubernetes/prometheus-service.yml",
        "kubectl apply -f ./kubernetes/service.yml"
    ]
    
    # Apply all kubectl commands
    for command in commands:
        apply_kubectl_command(command)

if __name__ == "__main__":
    main()
