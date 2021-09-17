# CS225 | On your own machine

In this guide, we will go over how to properly set up your machine so that you can run CS 225 code in the least hassle possible! There are 3 main ways of doing so: 
1) SSH through VSCode
2) Docker
3) Fast X

### Pros/Cons
|          | Pros                 | Cons |
| :------- | :------------------- | :------------------ |
| VSCode SSH  | Fast, less resource intensive| Internet connection req.       |
| Docker      | No internet, on local disk   | Resource intensive |
| Fast X      | Graphical UI*   | Fast internet        |

**Note: VSCode can display files like images, text, etc. as well*

Each of the above are ranked by which one should be easiest to use and makes the most sense.

## 1) SSH through VSCode

We will use Secure Shell (SSH) to help us access a Engineering Work Station (EWS) node through Visual Studio Code (VSCode). At UIUC, you can request compute resources through EWS with your NetID and use it to work on assignments from your classes. The reason we want to use an EWS server is because CS 225 runs test on EWS so you want to test your code with the tools you can and can't use. Let's get started.

Instructions:
1. **Download**: Download VSCode from [this](https://code.visualstudio.com/download) link. Please make sure you get the correct version for your operating system (OS). Follow the instructions to install the application.
https://code.visualstudio.com/download

    *Note: If you are confused whether to get the 64-bit or 32-bit version, you can check your computer's OS for the information. Most computers will use the 64-bit version.*


2. **Remote-SSH Extension**: Once you have it installed, please open the application up. You should see something like this:

    **[INSERT fig_1.png HERE]**

    On the left sidebar, click the icon with the 4 cubes (**[INSERT fig_2.png HERE]**). This should to the Add-On Extensions page. Please search for the "Remote-SSH" extension 

3. **Connecting to EWS**: To SSH into EWS, press the computer monitor icon that has appeared on your sidebar (**[INSERT fig_3.png HERE]**). 

    `SSH Targets` should be displayed near the top. If this is not the case, click on the drop down menu located at the top of this window, and select `SSH Targets`. It should look like this:

    **[INSERT fig_4.png HERE]**

    Mouse over `SSH Targets` and press the `+` button that pops up. 

    VSCode will then prompt you for the SSH target. 
    
    **[INSERT fig_5.png HERE]**
    
    Type in the following, replacing `[NETID]` with your NetID.

    
    ```
    [NETID]@linux.ews.illinois.edu
    ```

    Press `Enter` to confirm your input or `Escape` to cancel if you typed it incorrectly.

    VSCode will then prompt again in which file you would like to save the target. Pick the one underneath the `/Users/` directory:

    ```
    /Users/[YOUR USERNAME]/.ssh/config
    ```

    If everything worked, you will see a new SSH target pop up on the left window called `linux.ews.illinois.edu`. Here is another picture to verify with:

    **[INSERT fig_6.png HERE]**

4. **Opening a new window**: Mouse over the `linux.ews.illinois.edu` target and you should see a small button pop up on the right (**[INSERT fig_7.png HERE]**). Click on it.

    A new VSCode window should pop up and automatically attempt to connect to the remote EWS server through SSH. Wait a moment and it will prompt you to enter a passcode. 
    
    Enter your Illinois passcode associated with your NetID. It will load up the window and connect to your SSH. If it is not working, makes sure you have correctly typed your passcode and correctly spelled the SSH target (see 3).

Now you should be fully connected to EWS through SSH on VSCode and can use VSCode as if it were on your own computer. The only thing that will be different is that you are accessing the files of the target computer rather than your local computer.

## 2) Docker
**WARNING! Docker may not work on M1 Macs.**

1) **Installing Docker:** Please install the correct Docker depending on your OS.
    - For Windows:
    - For Mac:
    - For Linux: 














https://www.markdownguide.org/extended-syntax/