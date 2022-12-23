# Foundation Exam: International Software Testing Qualifications Board

## Introduction

### Why ISTQB
ISTQB is one of the world's most recognized certifications for software testing. In the last few years, it has become the standard for most applicants looking to break into the world of testing. The ISTQB offers testers a standardized set of terms, processes, and procedures that finesse our curious mind and book finding abilities. And whilst anyone absolutely can become a software tester without it, ***ISTQB foundation level certificate*** show us how we can elevate our application to the top of the pile.

### Terminology is key
 The terminology within the ISTQB Foundation is very **particular** and **precise** for a reason. This assures that all testers that go through the foundation level of the ISTQB have the same understanding of the terminology. Regardless if that test their experience level or career background, if they've been through the ISTQB Foundation, they should have the same definition, for example, of the term *acceptance criteria*. It also allows for clearer understanding between similar words and terms. Without understanding the *ISTQB glossary*, the terms *bug*, *defect*, and *error* may all be used interchangeably to describe the same situation when finding a problem in a piece of software. With the glossary, we were given a clear definition between the three, and can then associate these definitions to different scenarios that they would belong to. This is incredibly important with the ISTQB Foundation exam paper. Within the exam, there will usually be answers that are very close to being correct, but may use slightly different or similar terminology to try and trick us up. Understanding the terminology within the ISTQB foundation coursework will mean that we will recognize the incorrect answers based on our understanding of the terms used.

### Learning objective types and how to use them
 The work within the ISTQB Foundation Software Tester coursework and the syllabus can be broken into *learning objectives*. These learning objectives, also known as *cognitive levels of knowledge*, help to measure how well a tester should understand this information and what the tester may need to do with it once the tester recall it. There are three levels of learning objective.

 - #### K1: Remember - To recognize and recall ISTQB Term
   K1 looks at the candidate's ability to recognize, remember, and recall a term or concept. This could in theory apply to all of the work within the course and the syllabus. However, specific examples of the K1 learning objective can be: identify typical objectives of testing, being able to recognize the definition of failure within the ISTQB glossary, define risk level by using the likelihood and impact.

 - #### K2: Understand - To understand the reasons/statements behind ISTQB Term
   K2 looks at the candidate's ability to select the reasons or explanations for statements relating to a topic and can summarize, compare, classify, categorize, and give examples for the testing concept. Some examples of the K2:Understand learning objectives in the syllabus can include: distinguishing between the root cause of a defect and its effects, explaining the impact of context on the test process, and explaining the differences and similarities between integration and system testing.

 - #### K3: Apply - To apply the concept explained in ISTQB Term
   K3 looked at the candidate's ability to select the correct application of a concept or technique and apply it to a given context. Some examples of this learning objective can include: identifying boundary values for valid and invalid partitions, writing a defect report, covering a defect found during testing, and applying a review technique to a work product to find defects. These three learning objectives cover the whole syllabus for the ISTQB Foundation Software Testing Certification.

## Fundamentals of Testing

### What is Testing
- There is a very common misconception that software testing is the act of using a piece of software or a system and reporting if it works. The reality is that there are many different sides to the testing process, including, but not limited to, *test planning*, *test execution*, *analyzing results*, *designing and implementing tests*, *reporting test progress*, *evaluating the **system under test***. 

   There is also the difference between: 
   - #### Dynamic Tesing: 
     If a *system* or *component* is under test, then it is known as a dynamic test. A form of dynamic testing can be the execution of a workflow within a system to ensure that it works, often seen as a normal testing activity.
   - #### Static Testing:
     If a system is not directly being used as part of the testing, then it is a static test. A form of static testing could be reading a technical description of the system that has not yet been created and asking questions that lead to changes in the design based on issues not yet introduced into the system. 

- Another misconception about software testing is that it focuses entirely on verifying the *user stories* and other *system requirements* created during the system's making. It's true that testing does focus on ensuring that a system meets certain requirements, but it also involves *validation* (This can include checking the system under test will meet user needs such as accessibility).

   For a typical project, the objectives of testing may include:
   - #### preventing defects by evaluating requirements
   - #### user stories
   - #### designs
   - #### and code
   - #### verifying if all specified requirements have been fulfilled
   - #### checking whether the system under test is complete
   - #### to validate if it works as the users and other stakeholders expect
   - #### to build confidence in the system under test
   - #### to find defects and failures, thus reducing the level of risk of inadequate software
   - #### to provide sufficient information to stakeholders to allow them to make informed decisions regarding the system under test
   - #### to comply with contractual, legal, or regulatory requirements or standards. 

3. Within testing it is also important to understand the difference between:
   - #### Testing: Executing tests can show failures that are caused by defects in the system
   - #### Debugging: Is the development activity that finds, analyzes, and fixes such defects. However, in *agile development* and in some other *software development life cycles*, testers maybe involved in debugging and component testing.

### Why is testing necessary?

- Rigorous testing of *components*, *systems* and their associated *documentation* can help reduce the risk of failures occurring. 
- When defects are detected and subsequently fixed, this contributes to the quality of the components or system overall which results in a better product being produced.
- software testers may also be required to meet contractual or legal requirements or industry specific standards with their testing. 

So what are some of testing's contributions to software success?

- Having testers involved in the review of requirements or user stories could detect defects in these work products. The identification and removal of requirements defects reduces the risk of incorrect or untestable features being developed.

- Having testers work closely with the system designers while the system is being designed can increase each party's understanding of the design and how to test it. This can reduce the risk of fundamental design defects and enable tests to be identified at an early stage.

- Having testers work closely with developers while the code is under development can increase each part is understanding of the code and how to test it. This can further reduce the risk of defects within the code and the tests.

- Having tester's verify and validate the software prior to release can detect failures that might otherwise have been missed and support the process of removing defects that caused the failures. This increases the likelihood that the software will meet stakeholder needs and satisfy requirements.

It's also important to highlight that testing is not the same as quality assurance, though they are related:
- #### Quality Assurance:
  Within the larger concept of quality management, quality assurance is typically focused on the adherence to proper processes in order to provide confidence that the appropriate levels of quality will be achieved.

- #### Testing:
  System testing activities are part of the overall software development or maintenance process. Since quality assurance is concerned with the proper execution of the entire process, quality assurance supports proper testing. 
  
It's important to remember that whilst we usually use these terms interchangeably, *error*, *defect* and *failure* are actually quite different within the ISTQB glossary:

- #### Error and Defect (Cause and Effect):
  A person can make an error or mistake which can lead to the introduction of a defect or a bug in the software code or in some other part of the system. An error that leads to the introduction of a defect in one work product can trigger an error that leads to the introduction of a defect in a related work product.
  
  For example, an error in the requirements of a component of the system can introduce a requirements defect. This can then result when a coding error that leads to the defect in the code.
  
- #### Failure:
  A failure is the result of that defective code being executed. The root cause of this defect was the error in the requirements. And the effect of this error would have been the customer complaint about the system not working as they expected. 
  
Errors can occur for a number of different reasons, including but not limited to:

- #### Time pressures
- #### Human fallibility
- #### Inexperienced or insufficiently skilled project participants
- #### Miscommunication between project members
- #### Code complexity
- #### Misunderstandings about interest system interfaces
- #### New unfamiliar technologies. 

In addition to failures caused due to the defects in the code, failures can also be caused by *environmental conditions*. For example, radiation, electromagnetic fields and pollution can cause defects in firmware or influence the execution of software by changing hardwares conditions.

### The Seven Principles of Testing
Over the last 50 years or so, a lot of testing principles have been suggested, and they offer general guidelines for each tester. This is culminated in the *seven principles of software testing*:

1. #### Testing shows the presence of Defects, not their absence
   This means that testing can show that defects are present, but not that a system is ever defect-free. Testing reduces the probability of undiscovered defects remaining within a system, but even if zero defects are found, it does not prove complete correctness.

2. #### Exhaustive testing is impossible
   Testing absolutely everything is impossible. Rather than trying to test exhaustively, risk analysis, test techniques and priorities should be used to focus the testing effort.

3. #### Early testing saves time and money
   Both static and dynamic test activities should be started as early as possible in the software development lifecycle to find defects as soon as possible. Early testing is sometimes referred to as shift-left testing. Testing early in the software development lifecycle helps reduce or eliminate very costly changes.

4. #### Defects cluster together
   A small number of modules usually contain most of the defects discovered during pre-release testing or is responsible for most of the operational failures. Predicted defect clusters, and the actual observed defect clusters in test or operation are an important import into a risk analysis used to focus the testing effort.

5. #### Beware the pesticide paradox
   If the same tests are repeated over and over again, eventually these tests no longer find any new defects. To detect new defects, existing tests and test data may need changing, and new tests may need to be written. In some cases, such as automated regression testing, the pesticide paradox has a beneficial outcome, which is a relatively low number of regression defects.
   
6. #### Testing is context dependent
   Testing is done differently in different contexts. For example, safety critical industry control software is tested completely differently from an e-commerce mobile app. As a further example, testing in an Agile project is also done differently than testing in a Waterfall software development lifecycle project.

7. #### Absence of errors is a fallacy
   Some organizations expect the testers can run all possible tests and find all possible defects, but principles two and one respectively, tell us that this is impossible.
   
   Further, it is a fallacy to expect that just finding and fixing a large number of defects will ensure the success of a system. 
   
   For example, thoroughly testing all specified requirements and fixing all defects could still produce a system that is difficult to use, that does not fulfill the user's needs and expectations or that it is inferior compared to other competing systems.
   
The seven principles of testing cover a wide range of topics. And as part of the ISTQB, it's important to remember these, and their meanings.

### The Test Process
There is no one universal software test process, but there are common sets of test activities without which testing will be less likely to achieve its established objectives. These sets of test activities are our *test process*. 

The proper specific software test process in any situation depends on many factors:

- Which test activities are involved in the test process
- How these activities were implemented
- The activities may be discussed in the organization's test strategy.

Contextual factors that influence the test process for an organization include but aren't limited to:

- Software development lifecycle models and project methodologies being used
- Test levels and test types being considered
- Product and project risks
- The business domain
- Operational constraints, such as budgets, timescales, complexity, and contractual or regulatory requirements, organizational policies and practices, and required internal and external standards.

Although many of the Test Process main activity groups may appear logically sequential, they are often implemented iteratively. For example, Agile development involves small iterations of software design, build, and tests that happen on a continuous basis supported by ongoing planning.

A test process can consist of the following main groups of activities:

- #### Test planning
  Test planning involves activities that define the objectives of testing and the approach for meeting test objectives.

- #### Test monitoring and control
  Test monitoring involves the ongoing comparison of actual progress against planned progress using any test monitoring metrics defined in the test plan.

  Test control involves taking actions necessary to meet the objectives of the task plan.

  Test monitoring and control are supported by the evaluation of exit criteria, which are referred to as the definition of done in some software development lifecycle models.

- #### Test analysis
  During test analysis, the system under test is analyzed to identify testable features and define associated task conditions. In other words, test analysis determines what to test in terms of measurable coverage.

- #### Test design
  During test design, the test conditions are elaborated into high-level test cases and sets of high-level test cases. So test analysis answers the question what to test while test design answers the question how to test.

  Identifying necessary test data to support test conditions and test cases also falls under the test design category, and designing the test environments and identifying any required infrastructure and tools.

- #### Test implementation
  During test implementation, the testware necessary for test execution is created and/or completed including sequencing the test cases into test procedures. So test design answers the question how to test while test implementation answers the question do we now have everything in place to run the tests? Test implementation also includes the following major activities:

  - Developing and prioritizing test procedures and potentially creating automated test scripts
  - creating test suites from test procedures
  - preparing test data and ensuring that it is properly loaded into the test environment.

- #### Test execution
  During test execution, test suites are run in accordance with the test execution schedule, recording the IDs and versions of the test items or test objects, test tools and testware.

  Executing tests either manually or by using test execution tools. Comparing actual results with the expected results, and logging the outcome of test execution.

- #### Test completion
  Test completion activities collect data from completed test activities to consolidate any relevant information. Test completion usually includes the following major activities:

  - checking whether all defect reports are closed
  - entering change requests or product backlog items for any defects that remain unresolved at the end of test execution
  - creating a test summary report to be communicated to stakeholders
  - finalizing and archiving the test environments
  - the test data and test infrastructure
  - as well as any other testware for later reuse
  - handing all of the testware over to the maintenance teams
  - other project teams or other stakeholders who could benefit from its use - using the information gathered to improve the general test process maturity.  

### The Psychology of Testing
Software development, including software testing, involves human beings, therefore, human psychology plays an important part in software testing.

Identifying defects during requirements review, or a dynamic test execution, may be perceived as criticism of the product or its author. 

An element of human psychology called *confirmation bias* can make it difficult to accept information that disagrees with currently held beliefs. 

For example, since developers expect their code to be correct, they have a confirmation bias that makes it difficult to accept that their code is incorrect. 

In addition to confirmation bias, other cognitive biases may make it difficult for people to understand or accept information produced by testing. 

Furthermore, it is a common human trait to blame the bearer of bad news, and information produced by testing often contains bad news. To help combat this, information regarding defects and failures should be communicated in a constructive way. This way, tensions between project members can be reduced. 

Testers and their test managers need to have good interpersonal skills to be able to communicate effectively about defects, failures, results, progress and risks, and to build positive relationships with colleagues. 

Ways to communicate well include the following examples:
- Start with collaboration rather than battles.
- Remind everyone of the common goal of better quality systems. 
- Emphasize the benefits of testing.
- For the organization, defects found and fixed during testing will save time and money and reduce overall risk to product quality. Communicate test results and other findings in a neutral fact-focused way without criticizing the person who created the defective item. 
- Try to understand how the other person feels and the reasons they may react negatively to the information and confirm that the other person has understood what has been said and vice versa. 
- Developers and testers often think differently. The primary objective of development is to design and build a product. The objective of testing includes verifying and validating the product, finding defects prior to release and so forth.
  
  These are different sets of objectives, which require different mindsets. Bringing these mindsets together helps to achieve a higher level of product quality. A mindset reflects an individual's assumptions and preferred methods for decision-making and problem-solving. 
  
  A tester's mindset should include:
  - curiosity
  - professional pessimism
  - a critical eye
  - attention to detail
  - a motivation for good and positive communication and relationships.