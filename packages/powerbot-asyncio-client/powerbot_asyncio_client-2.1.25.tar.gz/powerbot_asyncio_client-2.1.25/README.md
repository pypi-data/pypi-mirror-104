![PowerBot Logo](https://www.powerbot-trading.com/wp-content/uploads/2018/03/PowerBot_Weblogo.png "PowerBot")

# **PowerBot Clients**

This repository serves as a way to host and publish PowerBot clients.

### Checklist

The following checklist outlines the necessary steps to take in order to publish a new version of the PowerBot Clients for Python.

Prerequisite: Make sure you have a functioning version of the Swagger Codegen client available. You find installation and usage instructions in
the [official GitHub](https://github.com/swagger-api/swagger-codegen) repository for the project.

1. Get the latest PowerBot Swagger API specification yaml file.
2. Use the configuration files provided in the [configs](configs) directory to generate two Python clients, one based solely on urllib3 and one built
   for asyncio.
3. Perform local tests to ensure that everything works as expected (e.g. imports, model names).
4. Replace the old clients in this repo with the newly generated ones.
5. Update both setup files (e.g. bump version number to match API specification). Make sure that the clients are compatible with the specified
   dependency versions.
6. Commit and push the changes. This will trigger a GitHub Workflow, which automatically uploads both packages to test.pypi.
7. Make sure that the jobs ran successfully. Test that the packages have been published to test.pypi as intended.
8. Create a new release by tagging the latest commit with the version number of the API specification. This will trigger a GitHub Workflow, which
   automatically uploads both packages to the regular pypi.

