https://www.tutorialspoint.com/maven/maven_environment_setup.html


	1	If the SDK was installed automatically as part of Android Studio then it's located here: /Users/{YOUR_USER_NAME}/Library/Android/sdk
Once you know the location, open a terminal window and enter the following (changing out the path to the SDK to be however you installed it):
export ANDROID_HOME={YOUR_PATH}
Once you have this set, you need to add this to the PATH environment variable:
export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools
Lastly apply these changes by re-sourcing .bash_profile:
source ~/.bash_profile
	4	Type - echo $ANDROID_HOME to check if the home is set.
echo $ANDROID_HOME
