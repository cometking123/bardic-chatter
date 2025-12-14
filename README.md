# bardic-chatter
A python script to sing songs in Minecraft proper (for use in LoTC https://www.lordofthecraft.net/)

## How to use
After downloading the file, download all libraries based on the requirements file.


### 1. Installation
To import this for use, clone the repository using:

```bash
git clone https://github.com/cometking123/bardic-chatter.git
```
and then navigate to the directory that was imported. This is usually done using cd bardic-chatter

Once in the directory, import all requirement libraries using the below command

```bash
pip install -r requirements.txt
```

### 2. Deployment

Review bardic-chatter.py, and replace the proceed_key and exit_key with a key of your choice. This controls how you will run through each line of a story and, if possible, to cancel it

When importing a file, copy each line as if you are typing it within the LoTC minecraft server. This includes any chat modes (#q, #s, #rp), emotes (**, *), and punctuation. It will be written exactly as provided! For an example, see seeshanty.txt

Once imported, place it under the "Poems" folder. Anything outside of this folder will not be viewable to the program

### Running the Program

Inside your terminal input the following line:

```bash
python bardic-chatter.py
```

You will then see a prompt to input the poem title to recite. 

Once provided, click on the proceed_key to run through the story. Make sure your active window is Minecraft (To mark a window as active, click or tab into the Minecraft window)

Once the tale is finished, it will exit the program.

## Feedback?
Feel free to open an issue, or DM me directly on LoTC servers at [cometking123](https://www.lordofthecraft.net/profile/21637-cometking123/)