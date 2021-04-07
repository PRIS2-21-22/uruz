# uruz

## Material and methods

For this lab session, we will implement in Python the assigned ADT (Polygon in this case), and upload it to a GitHub repository in the organization. Then, working in pairs, we must review the code of our partner using two tools, SonarCloud and Codacy. For communicating the issues, in the workflow followed we also used GitHub issues for a better tracking of them. Finally, after finishing the review, each of us must refactor the code using the feedback from our partner and the mentioned tools.

## Code review

### SonarCloud

![](https://i.imgur.com/vQE8lAr.png)

If we take a look to the general overview of the individual project #1 (Polygon), we do not observe any alarming issues with our code. We can note, however, that 2 classes (Punto and Vector) are lacking any comments which could hinder future.

We can also notice the high number of branches in the class Poligono, but that is due to it being the core of the project and the longest file with 68 lines. With a 7.4% of comment lines we can tell that such complexity is well documented.

The last issue that we can find is the big amount of statements per method in the class UsoPoligono, in fact it is composed of just one method with 37 statements.

![](https://i.imgur.com/17KHELr.png)

If we take a deeper look, however, we can see this is indeed the main class of our project and it is composed of up to 24 different calls to other methods. Still, it is likely that the number of calls could be reduced or that it could be broken down into smaller sub-methods.

### Codacy

![](https://i.imgur.com/TvdIKnR.png)

If we take a look at the Kiviat graph for our project, we can easily see the general strength and weaknesses of the project. We can see that the average complexity is low, which is generally a good sign, however the average depth is as high as 1.69 which means most lines in our code are at least at one level of depth and some of them at two levels. This could be a sign that refactorization could help simplify the code. The rest of the parameters are pretty normal, worth noting that we only have 4.38 statements on average per method but that's likely due to the code not being overly complex.

### GitHub issues

## Versioned project

### General overview

![](https://i.imgur.com/Tz8EsV7.png)

Once we manually add into SourceMonitor the 4 different versions or checkpoints that make up our versioned project, we can get an overview of each of the iterations. In this general overview we can see how our metrics don't vary wildly from one version to the next one.

![](https://i.imgur.com/BSmQgbU.png)

It is worth noting, however, how the average statements per method is constantly reduced, while the methods per class steadily increase. This is generally a good sign that proper refactorization is being made as bigger methods are being broken down into more manageable ones. We can see how the average depth and complexity also decrease as a sign of this.

![](https://i.imgur.com/YLygrNi.png)

However, we also need to realize that the last version removed a lot of documentation and commment lines from the code. The number of lines is almost static across all versions but the percentage of comments dropped to 4.0% to 1.6% in the last iteration. This could be a sign that some unneeded commentaries were removed after the refactorization, but still only 1 line of comments per 100 lines of code is a low percentage.

### Kiviat Graph

![](https://i.imgur.com/FRbz0L1.png)

Next we will take a look at the Kiviat graph, in this case for the last iteration of the project (note that there is a bug with SourceMonitor and we had to select the first baseline to get the metrics that actually correspond to the last version).

In this case we can see at a glance how the number of comment lines is really low in this final version. On the other hand, each method is kept really concise with a low number of statements per method and the average complexity is reduced, although the maximum complexity and depth could signal that some further refactoring could be attempted on some of the denser methods.

## Review

To sum up, SourceMonitors offers a pretty simple way to visualize some of the simpler metrics of code that can measure the quality of it. However, it is quite a limited tool as it doesn't even allow projects with code in different languages. It also had some notable bugs when working with several checkpoints so it may be best suited for small projects.
