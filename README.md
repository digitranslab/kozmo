Kozmo is an open-source LLM app development platform. Its intuitive interface combines agentic AI workflow, RAG pipeline, agent capabilities, model management, observability features and more, letting you quickly go from prototype to production. 

## Quick start
> Before installing Kozmo, make sure your machine meets the following minimum system requirements:
> 
>- CPU >= 2 Core
>- RAM >= 4 GiB

</br>

The easiest way to start the Kozmo server is through [docker compose](docker/docker-compose.yaml). Before running Kozmo with the following commands, make sure that [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) are installed on your machine:

```bash
cd kozmo
cd docker
cp .env.example .env
docker compose up -d
```

After running, you can access the Kozmo dashboard in your browser at [http://localhost/install](http://localhost/install) and start the initialization process.

#### Seeking help
Please refer to our [FAQ](https://docs.kozmo.ai/getting-started/install-self-hosted/faqs) if you encounter problems setting up Kozmo. Reach out to [the community and us](#community--contact) if you are still having issues.

> If you'd like to contribute to Kozmo or do additional development, refer to our [guide to deploying from source code](https://docs.kozmo.ai/getting-started/install-self-hosted/local-source-code)

## Key features
**1. Workflow**: 
  Build and test powerful AI workflows on a visual canvas, leveraging all the following features and beyond.


  https://github.com/digitranslab/kozmo/assets/13230914/356df23e-1604-483d-80a6-9517ece318aa



**2. Comprehensive model support**: 
  Seamless integration with hundreds of proprietary / open-source LLMs from dozens of inference providers and self-hosted solutions, covering GPT, Mistral, Llama3, and any OpenAI API-compatible models. A full list of supported model providers can be found [here](https://docs.kozmo.ai/getting-started/readme/model-providers).

![providers-v5](https://github.com/digitranslab/kozmo/assets/13230914/5a17bdbe-097a-4100-8363-40255b70f6e3)


**3. Prompt IDE**: 
  Intuitive interface for crafting prompts, comparing model performance, and adding additional features such as text-to-speech to a chat-based app. 

**4. RAG Pipeline**: 
  Extensive RAG capabilities that cover everything from document ingestion to retrieval, with out-of-box support for text extraction from PDFs, PPTs, and other common document formats.

**5. Agent capabilities**: 
  You can define agents based on LLM Function Calling or ReAct, and add pre-built or custom tools for the agent. Kozmo provides 50+ built-in tools for AI agents, such as Google Search, DALL·E, Stable Diffusion and WolframAlpha.

**6. LLMOps**: 
  Monitor and analyze application logs and performance over time. You could continuously improve prompts, datasets, and models based on production data and annotations.

**7. Backend-as-a-Service**: 
  All of Kozmo's offerings come with corresponding APIs, so you could effortlessly integrate Kozmo into your own business logic.


## Using Kozmo

- **Cloud </br>**
We host a [Kozmo Cloud](https://kozmo.ai) service for anyone to try with zero setup. It provides all the capabilities of the self-deployed version, and includes 200 free GPT-4 calls in the sandbox plan.

- **Self-hosting Kozmo Community Edition</br>**
Quickly get Kozmo running in your environment with this [starter guide](#quick-start).
Use our [documentation](https://docs.kozmo.ai) for further references and more in-depth instructions.

- **Kozmo for enterprise / organizations</br>**
We provide additional enterprise-centric features. [Log your questions for us through this chatbot](https://kozmo.app/chat/22L1zSxg6yW1cWQg) or [send us an email](mailto:business@kozmo.ai?subject=[GitHub]Business%20License%20Inquiry) to discuss enterprise needs. </br>
  > For startups and small businesses using AWS, check out [Kozmo Premium on AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-t22mebxzwjhu6) and deploy it to your own AWS VPC with one-click. It's an affordable AMI offering with the option to create apps with custom logo and branding.


## Staying ahead

Star Kozmo on GitHub and be instantly notified of new releases.

![star-us](https://github.com/digitranslab/kozmo/assets/13230914/b823edc1-6388-4e25-ad45-2f6b187adbb4)


## Advanced Setup

If you need to customize the configuration, please refer to the comments in our [.env.example](docker/.env.example) file and update the corresponding values in your `.env` file. Additionally, you might need to make adjustments to the `docker-compose.yaml` file itself, such as changing image versions, port mappings, or volume mounts, based on your specific deployment environment and requirements. After making any changes, please re-run `docker-compose up -d`. You can find the full list of available environment variables [here](https://docs.kozmo.ai/getting-started/install-self-hosted/environments).

If you'd like to configure a highly-available setup, there are community-contributed [Helm Charts](https://helm.sh/) and YAML files which allow Kozmo to be deployed on Kubernetes.

- [Helm Chart](https://github.com/douban/charts/tree/master/charts/kozmo)
- [Helm Chart](https://github.com/BorisPolonsky/kozmo-helm)
- [YAML file](https://github.com/Winson-030/kozmo-kubernetes)

#### Using Terraform for Deployment
Deploy Kozmo to Cloud Platform with a single click using [terraform](https://www.terraform.io/)

##### Azure Global
- [Azure Terraform by @nikawang](https://github.com/nikawang/kozmo-azure-terraform)

##### Google Cloud
- [Google Cloud Terraform by @sotazum](https://github.com/DeNA/kozmo-google-cloud-terraform)

#### Using AWS CDK for Deployment
Deploy Kozmo to AWS with [CDK](https://aws.amazon.com/cdk/)

##### AWS 
- [AWS CDK](https://github.com/aws-samples/solution-for-deploying-kozmo-on-aws)
