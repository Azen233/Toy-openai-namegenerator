![view](pic.png)


This is a first name generator app using the OpenAI API, modified from example Openai app
## Setup


1. Create a new virtual environment:

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

2. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```

3. Make a copy of the example environment variables file:

   ```bash
   $ cp .env.example .env
   ```

4. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file.

5. Run the app:

   ```bash
   $ flask run
   ```
