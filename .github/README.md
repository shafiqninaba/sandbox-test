# GitHub Actions Workflow

## Data Analysis Tool Workflow

This workflow automatically runs the `run.sh` script whenever code is pushed to the main branch or when a pull request is opened.

### What it does:

1. **Environment Setup**: Sets up Python 3.12 and caches pip dependencies
2. **Script Execution**: Runs the data analysis tool in multiple modes:
   - Default mode (attempts to fetch external data)
   - Mock data mode (generates local test data)
   - Matrix generation (creates random numerical matrices)
   - Export mode (saves results to JSON file)

3. **Artifact Collection**: Automatically uploads any generated `results.json` files as workflow artifacts

### Triggers:
- Push to `main` branch
- Pull requests targeting `main` branch  
- Manual workflow dispatch (can be triggered manually from GitHub Actions tab)

### Output:
- Console logs showing the analysis results
- `results.json` artifact (when export option is used)

The workflow is designed to validate that the data analysis tool works correctly across different scenarios and configurations.