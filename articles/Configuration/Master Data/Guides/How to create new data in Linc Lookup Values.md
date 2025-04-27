---
grand_parent: Master Data
has_children: false
layout: default
nav_order: 21901
parent: Guides
title: How to create new data in Linc Lookup Values
---

# How to create new data in Linc Lookup Values


### In this guide  

[Quick Overview](#quick-overview)  
[Add new Linc Lookup Value master data where no parent is required](#add-new-linc-lookup-value-master-data-where-no-parent-is-required)  
[Add new Linc Lookup Value master data where a parent is required](#add-new-linc-lookup-value-master-data-where-no-parent-is-required)  

Related articles
<br/>
[Linc Lookup Values](/articles/Configuration/Master%20Data/Linc%20Lookup%20Values)

---
## Quick Overview
<br/>
Linc Lookup Values is where most master data relating to produce and logistics live. This includes things like producer codes (PUCs), variety codes, packhouse codes, transport methods, pallet base and heights, inspection points, and so forth.

For more in-depth information on Linc Lookup Values (including a list of all the types of master data that is stored in this table) please read our documentation article on [Linc Lookup Values](/articles/Configuration/Master%20Data/Linc%20Lookup%20Values)  

From time to time, you may need to add new master data records in this table � for instance when you start receiving pallets from a new packhouse and the packhouse code does not yet exist in your master date; or when a new variety code is being packed that you must add to Linc Lookup Values.

In this step-by-step guide we will:

- Show you how to add a new master data record in Linc Lookup Values for master data that does not have a parent
- Show you how to add a new master data record in Linc Lookup Values for master data that does have a related parent  


**What do we mean with "parents"?**  
<br/>
Some master data has to exist in relationship to a parent. An example of this is Commodity Code for which the parent is Commodity Group Code. The commodity "apples" belong to the parent commodity group "pome fruit". This parent-child relationship ensures that an apple pallet cannot be created with a Commodity Group of say Grapes or Citrus. 

---  

## Add new Linc Lookup Value master data where no parent is required  
<br/>
In our example below, we are going to add a new Packhouse Code.  

### STEP 1

Use the search tool (magnifying glass) in Business Central to navigate to Linc Lookup Values

![](/media/Configuration_MasterData_Guide_LLV_1.%20Select%20the%20search%20box.jpeg)

### STEP 2

Start typing _Linc Lookup Values_ below "Tell me what you want to do". 
As you type, the system will start searching for pages that match what you are looking for. 
Select **Linc Lookup Values** when it shows up.

![](/media/Configuration_MasterData_Guide_LLV_2.%20Navigate%20to%20Linc%20Lookup%20Values.jpeg)

### STEP 3

In the Linc Lookup Values page, select the filter icon. This will open the filter pane in the left side of the page.

![](/media/Configuration_MasterData_Guide_LLV_3.%20Select%20filter%20in%20Linc%20Lookup%20Values.jpeg)

### STEP 4

Click on **+ Filter** and then choose **Lookup Field Name**. By first filtering Linc Lookup Values for the type�of master data you want to add, you will minimise errors when creating a new record.

![](/media/Configuration_MasterData_Guide_LLV_4.%20Open%20filter%20options%20in%20Linc%20Lookup%20Values.jpeg)

![](/media/Configuration_MasterData_Guide_LLV_5.%20Choose%20to%20filter%20by%20Lookup%20Field%20Name.jpeg)

### STEP 5

Start typing the name of the Linc Lookup Field for which you want to add a new master data record. As you type, the list of available options will start appearing. Once you see the appropriate Name, click on it.
In our example, we will start typing "Packhouse Code" and then select it from the available options in the list.

![](/media/Configuration_MasterData_Guide_LLV_6.%20Find%20the%20relevant%20Lookup%20Field%20Name.jpeg)

### STEP 6

Click on **+ New** in the page menu. This will insert an empty new record; but because you have already filtered the Linc Lookup Values for the **Lookup Field Name** (in our example Packhouse Code), the system expects that you want to add a new record for that specific Lookup Field Name and automatically fills that in for you.

![](/media/Configuration_MasterData_Guide_LLV_7.%20Choose%20New%20to%20add%20new%20record.jpeg)

This is what your page will now look like:

![](/media/Configuration_MasterData_Guide_LLV_8.%20New%20empty%20record%20created.jpeg)

### STEP 7

Add the new **Code** and **Description**.

![](/media/Configuration_MasterData_Guide_LLV_9.%20Add%20new%20code%20and%20description.jpeg)

### STEP 8

Note that your page will show **Not Saved** in the top right corner after you have added the code and description. Before you leave the page, ensure that your record is saved. Simply click on any other record (line), check that it then shows **Saved** in the top right corner.

If you need to add more than one new master data record, simply repeat steps 4 through 8 before you close the page.

![](/media/Configuration_MasterData_Guide_LLV_10.%20Ensure%20record%20is%20saved%20and%20close.jpeg)

---

## Add new Linc Lookup Value master data where a parent is required  
<br/>
In our example below, we are going to add a new Variety Code. Variety Codes are linked to parent Variety Group Codes. 

### STEP 1

Navigate to Linc Lookup Values and filter for the relevant **Lookup Field Name** (in our example, we have filtered to Variety Code).
Then choose **+ New** in the page menu to create a new empty record.

![](/media/Configuration_MasterData_Guide_LLV_11.%20New%20with%20Parent%20-%20choose%20New.jpeg)

This is what your page with the new "empty" record will now look like: the **Lookup Field Name** is already populated based on the Lookup Field Name you have filtered for.

![](/media/Configuration_MasterData_Guide_LLV_12.%20New%20with%20parent%20-%20new%20empty%20record.jpeg)


### STEP 2

Start typing the name of the **parent** in **Parent Lookup Field Name**. 

_Tip: look at other master data records for the same Lookup Field Name for which you are adding master data to double-check what the correct Parent Lookup Field Name must be._
As you type, the system will start searching for the Parent Lookup Field Name based on what you type.

When you see the correct Parent Lookup Field Name in the list, select it. 

![](/media/Configuration_MasterData_Guide_LLV_13.%20New%20with%20parent%20-%20select%20parent%20lookup.jpeg)

### STEP 3

For master data records that **do** have parents, you must first specify the Parent Code before you enter the Code for your new record.
In our example we are adding a new pear variety; so we first choose �PR� (Pears) as the parent Variety Group Code.

![](/media/Configuration_MasterData_Guide_LLV_14.%20New%20with%20Parent%20-%20select%20parent%20code%20first.jpeg)

### STEP 4

Now type in the new **Code** and **Description**.

![](/media/Configuration_MasterData_Guide_LLV_15.%20New%20with%20Parent%20-%20add%20code%20and%20description.jpeg)

### STEP 5

Note that your page will show **Not Saved** in the top right corner after you have added the code and description. Before you leave the page, ensure that your record is saved. Simply click on any other record (line), check that it then shows **Saved** in the top right corner.

If you need to add more than one new master data record, simply repeat steps 1 through 5 before you close the page.

![](/media/Configuration_MasterData_Guide_LLV_16.%20New%20with%20parent%20-%20save%20and%20close.jpeg)

---