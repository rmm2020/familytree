# familytree
## Summary
Python code to generate family tree diagram and ancestor charts. Should be useable by others to generate their own family tree. Customizable visuals (font, canvas sizing, background, frames, image sizing, etc.). Family tree image generated using Pillow and ancestor diagrams/charts generated with combination of Matplotlib, Pillow, and Cartopy

## Overview
This project was made for the purpose of visualizing my own family tree so that I could make changes, such as adjusting which people were being shown (e.g. include cousins or not) and play around with aesthetics like overall canvas dimensions or fonts, and easily re-generate the image. In the future if I want to print a different size, or update photos, or add death years, or add new kids people have, then it will be easy to do and re-print the photo to hang in my frame. 

![my tree](/ExampleImages/Example_mytree.png)

![my tree2](/ExampleImages/Example_mytree2.png)

![harry potter tree](/ExampleImages/Example_variations2.png)

### Family Tree Structure
The program was testing using my own family tree data, but should be fairly applicable to other peoples’ trees if anyone wants to try using pieces of it. I would also be happy to help apply it or troubleshoot if anyone tries working with it. 

It can do a classic Descendants Chart with everyone branching down from 1 person at the top, or an Ancestor Chart with people branching up from 1 person at the bottom, or a bit of a hybrid focused on someone in the middle and showing generations above and below. 

![descendant tree](/ExampleImages/Example_descendanttree.png)

![ancestor tree](/ExampleImages/Example_ancestortree.png)

![hybrid tree](/ExampleImages/Example_hybridtree.png)

It can also handle some amount of other kinship relationships, showing siblings of upper generations and cousins, etc. You do run into an issue trying to have too many “sideways” relationships showing because it cannot place people and visualize correctly. 

![kinship tree](/ExampleImages/Example_kinship_annotated.png)

It can handle some half-siblings (automatically by parent-child relationship) or step-siblings (by manual inclusion entry)

### Technology Used 
The project is all programmed in Python using **pandas** to read the initial data and **pillow** to manipulate and overlay photos, text, and line features onto the final image. The family tree data is read from an excel sheet. 
The additional graphic visuals use a combination of **matplolib**, **pillow**, and **cartopy** to generate. 

## Family Tree Image
### User Configuration
Config.py file contains user input configuration dictionary that will help build out family tree (this way more than one family tree configuration can be saved and stored to easily generate new images). For example, I have a configuration for a tree centered around myself as well as a tree centered around my daughter (that has my husband's family included).

User inputs described in more detail in the comments in the code, but they include:
Selecting person0 (Core Person) to base the tree on and selecting the number of generations vertically up and down to include and degrees sideways to include

![vertside](/ExampleImages/Example_vert-side.png)

Optional exclusion list or inclusion list (I use the inclusion list for some step-children that wouldn’t show up otherwise, since they are not blood related to the person in the tree). People in inclusion list still need a parent (or parent of partner that is also included) to be included in the tree in order to be sorted properly.

Set photo scaling. Photos can all be the same size by setting equal scaling, or you can manually select the sizing for each degree vertically and sideways. For example, you could show lower generations larger, or the full core line of parents larger. 

![size1](/ExampleImages/Example_size1.png)

![size2](/ExampleImages/Example_size2.png)

![size3](/ExampleImages/Example_size3.png)

Set canvas dimensions, borders, spacing between different types of kin relationships, photo aspect ratio, text and ancestor text formatting, etc. 

### Family Data
Family data read from excel file. Format of excel table should match example excel sheets and have all the headers listed here:

![familydata](/ExampleImages/ExampleData1.PNG)

Parent relationships and partner relationships should all be by person key. Multiple partnerships entered by putting comma between partners in list and comma between partnership types. Partnership types (M-married, D-divorced, O-other). Ancestor text is used to describe top level or chart ancestors. 
It could be possible in the future to add Gedcom (standard  genealogy file type) importing instead of this excel format. 

![familydata2](/ExampleImages/ExampleData2.PNG)

### Code outline
* Read family database from excel file into pandas database. 
* Person Class created that will store person information (e.g. name, birthyear) and family information (e.g. father, mother, siblings, partners). 

  Later, information relating each person to the “Core Person” the tree is built off of (e.g. in core family line, generation level vs. Core Person) and picture placement on       image (e.g. pic x position, pic width) will be modified as well. 

  Loop through everyone in family database and create person class instances. Create family dictionary “famdict” that links the person ID to the person object.
* Find all people to include in tree
* Sort people starting from top generation down. Upper generation is sorted according to father/mother order in relation to person0 and then lower generations are all sorted       according to parent-child, partner, and sibling relationships and whether or not they are in core family line

  ![fathermother](/ExampleImages/Example_fathermotherorder.png)
  
* Determine some family counts that impact photo-sizing and placement
* Photo size/position and line placement
  * Determine size and position of all person photos
  * Determine all lines between partners and parents<->children
  * Shift lowest generation of children left/right to be centered below parents, if possible (no upper generations shifted in the code right now)
  * Shift vertical positioning of parent-children lines so as to not touch 
* Font, Background, Nameplate Frames, and Ancestor Text Frames can be modified

  ![variations](/ExampleImages/Example_variations1.png)
  
* Place all photos, text, and frames onto canvas (using re-size and text sizing adjustments as needed)

## Other Graphics/Charts
The other notebook file FamilyTree_Charts has code to create several genealogy graphics. The descriptions of the code are commented in the code itself.

### Data
Data is read from another excel file with a different structure (Example below). Most of the columns are straightforward. 

![ancestordata](/ExampleImages/ExampleData3.PNG)

* The genup column has a number listing the numer of generations up from the center that the ancestor is. For example, for the graphics for my daughter, she is listed as           genup=0, my husband and I are both genup=1, my parents are genup=2 and so on. This is the main number that the data gets filtered by for most of the charts as you loop through   the generations. 
* The movement column (used to generate traces on the maps) is entered as follows separated by ';' semicolons: Location 1; Location 2; Year Moved
  Multiple movements by one person can be entered using ' %% ' to separate, for example: Seattle, WA; Phoenix, AZ; 1997 %% Phoenix, AZ; Toronto, Ontario, Canada; 2008
* The occupation column (used for the occupation chart) is entered as follows separated by '%': Occupation Heading % Occupation description
  The occupation heading must match the headings used in the dictionary in the code. The description can be whatever you want. If you want to force a line break on the             description it should be done with '$$' symbol. 
  Example1: Human Services % Clergy
  Example2: Health Science % Nurse$$4 Children
  Example3: Manufacturing % Machinist$$Assembly Line Worker


### Genetic Ancestry Pie Chart

![ancestry pie](/ExampleImages/Example_ancestrypie.png)

### Birth Location by Generation

![birth location](/ExampleImages/Example_birthlocation.png)

### Occupation by Generation

![occupation](/ExampleImages/Example_occupation.png)

### Age at Marriage by Generation

![marriageage](/ExampleImages/Examplemarriageage.png)

### Years Lived by Generation

![years](/ExampleImages/Example_yearslived.png)

### Maps Showing Ancestor Movement and Origins

![worldmap](/ExampleImages/Example_worldmap.png)

![usamap](/ExampleImages/Example_usamap.png)

![annotated map](/ExampleImages/Example_europemapannotated.png)

  
