# reddit-vip-flairs

Bot to flair submissions that include replies by users of interest.

## Prerequisites

You'll need a reddit account as well as an application, which you can
create [here](https://www.reddit.com/prefs/apps/).

## Installation

Clone the repository:

    git clone https://github.com/schwarz/reddit-vip-flairs.git

Set up a virtual env for it and activate it:

    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

## Usage

Adjust the necessary environment variables, you can find all in `.env.example`.
Rename this file to `.env` to make reddit-vip-flairs load the variables in it.
Finally, run the script:

    python main.py

## License

reddit-vip-flairs is released under the [MIT License](https://opensource.org/licenses/MIT).
