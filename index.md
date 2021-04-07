# uruz

## Material and methods

For this lab session, we will implement in Python the assigned ADT (Polygon in this case), and upload it to a GitHub repository in the organization. Then, working in pairs, we must review the code of our partner using two tools, SonarCloud and Codacy. For communicating the issues, in the workflow followed we also used GitHub issues for a better tracking of them. Finally, after finishing the review, each of us must refactor the code using the feedback from our partner and the mentioned tools.

## Code review

### SonarCloud

![](https://i.imgur.com/pjykSpb.png)

SonarCloud allow us to keep track of bugs and code smells in our partner repository. In the image, we can see three of these code smells related to the naming convention of methods in Python. It is possible comment on them, alter their priority, assign someone to the task and even confirm them or flag as false positive.

![](https://i.imgur.com/QqOURO5.png)

If we take a look at the main overview, we can see a general review of the issues with the project, as well as an estimate on the time required to fix them. From this overview it is also possible to create several milestones in our project to keep track of the progress in the quality of its code.

### Codacy

![](https://i.imgur.com/TOCXtKB.png)

In Codacy, the second code review platform that we will use for this lab, we can also easily keep track of several issues with the code. It will scan the project every time a commit is made and automatically report on the quality of the updated code and issues introduced.

In the image, we can see the issues view. This section displays an overview of the issues present at the latest version of the code. From here, it is even possible to export them to GitHub issues as the corresponding repository.

### GitHub issues

![](https://i.imgur.com/PGb1e5s.png)

Beside this automated tools, it is also possible to manually point at bugs, enhancements or other suggestions on the project by creating a new issue on the corresponding repository.

In the example image, I have created a new issue in my partner repository for an enhancement he could introduce before refactoring. As it is shown, you can add tags, links, reference commits, other issues and assign members to it. After adding the enhancement, the issue was closed by my partner.

## Code refactoring

