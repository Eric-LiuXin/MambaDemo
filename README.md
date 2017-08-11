# MambaDemo
Demonstrate the use of mamba

## Build and Test

### Build/rebuild docker image

To build/rebuild the mamba_demo docker image, just run

    docker build -t mamba_demo .

### Run tests

Just run

    docker run mamba_demo  /bin/bash -c "mamba --enable-coverage"

### Get Coverage

Just run
    
    docker run mamba_demo  /bin/bash -c "coverage report"

### Get coverage html report

Just run
    
    docker run mamba_demo  /bin/bash -c "coverage html -d covhtml"
