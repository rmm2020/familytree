# familytree
## Summary
Python code to generate family tree diagram and ancestor charts. Should be useable by others to generate their own family tree. Customizable visuals (font, canvas sizing, background, frames, image sizing, etc.). Family tree image generated using Pillow and ancestor diagrams/charts generated with combination of Matplotlib, Pillow, and Cartopy

## Overview
This project was made for the purpose of visualizing my own family tree so that I could make changes, such as adjusting which people were being shown (e.g. include cousins or not) and play around with aesthetics like overall canvas dimensions or fonts, and easily re-generate the image. In the future if I want to print a different size, or update photos, or add death years, or add new kids people have, then it will be easy to do and re-print the photo to hang in my frame. 

### Family Tree Structure
The program was testing using my own family tree data, but should be fairly applicable to other peoples’ trees if anyone wants to try using pieces of it. I would also be happy to help apply it or troubleshoot if anyone tries working with it. 

It can do a classic Descendants Chart with everyone branching down from 1 person at the top, or an Ancestor Chart with people branching up from 1 person at the bottom, or a bit of a hybrid focused on someone in the middle and showing generations above and below. 

It can also handle some amount of other kinship relationships, showing siblings of upper generations and cousins, etc. You do run into an issue trying to have too many “sideways” relationships showing because it cannot place people and visualize correctly. 

It can handle some half-siblings (automatically by parent-child relationship) or step-siblings (by manual inclusion entry)

### Technology Used 
The project is all programmed in Python using **pandas** to read the initial data and **pillow** to manipulate and overlay photos, text, and line features onto the final image. The family tree data is read from an excel sheet. 
The additional graphic visuals use a combination of **matplolib**, **pillow**, and **cartopy** to generate. 

## Family Tree Image
### User Configuration
Config.py file contains user input configuration dictionary that will help build out family tree (this way more than one family tree configuration can be saved and stored to easily generate new images). For example, I have a configuration for a tree centered around myself as well as a tree centered around my daughter (that has my husband's family included).

User inputs described in more detail in the comments in the code, but they include:
Selecting person0 (Core Person) to base the tree on and selecting the number of generations vertically up and down to include and degrees sideways to include

Optional exclusion list or inclusion list (I use the inclusion list for some step-children that wouldn’t show up otherwise, since they are not blood related to the person in the tree). People in inclusion list still need a parent (or parent of partner that is also included) to be included in the tree in order to be sorted properly.

Set photo scaling. Photos can all be the same size by setting equal scaling, or you can manually select the sizing for each degree vertically and sideways. For example, you could show lower generations larger, or the full core line of parents larger. 

Set canvas dimensions, borders, spacing between different types of kin relationships, photo aspect ratio, text and ancestor text formatting, etc. 

### Family Data
Family data read from excel file. Format of excel table should match example excel sheets and have all the headers listed here:

Parent relationships and partner relationships should all be by person key. Multiple partnerships entered by putting comma between partners in list and comma between partnership types. Partnership types (M-married, D-divorced, O-other). Ancestor text is used to describe top level or chart ancestors. 
It could be possible in the future to add Gedcom (standard  genealogy file type) importing instead of this excel format. 


### Code outline
* Read Family Data
  Read family database from excel file into pandas database. 
* Person Class
  Person Class created that will store person information (e.g. name, birthyear) and family information (e.g. father, mother, siblings, partners). 

  Later, information relating each person to the “Core Person” the tree is built off of (e.g. in core family line, generation level vs. Core Person) and picture placement on       image (e.g. pic x position, pic width) will be modified as well. 

  Loop through everyone in family database and create person class instances. Create family dictionary “famdict” that links the person ID to the person object.
* Find all people to include in tree
* Sort people starting from top generation down. Upper generation is sorted according to father/mother order in relation to person0 and then lower generations are all sorted       according to parent-child, partner, and sibling relationships and whether or not they are in core family line
* Determine some family counts that impact photo-sizing and placement
* Photo size/position and line placement
  * Determine size and position of all person photos
  * Determine all lines between partners and parents<->children
  * Shift lowest generation of children left/right to be centered below parents, if possible (no upper generations shifted in the code right now)
  * Shift vertical positioning of parent-children lines so as to not touch 
* Font, Background, Nameplate Frames, and Ancestor Text Frames can be modified
* Place all photos, text, and frames onto canvas (using re-size and text sizing adjustments as needed)

