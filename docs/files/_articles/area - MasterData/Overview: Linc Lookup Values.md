# Overview: Linc Lookup Values

Most of produce and logistic related master data are maintained in Linc Lookup Values. Various tables, pages and features in ProduceLinc point to this master data to look up and validate values.

The Lookup Field Name defines the ‘type’ of master data field. This allows for a comprehensive list of master data, such as producer codes, packhouse code, shipping temperature codes, variety codes, etc. to be maintained in a single table – rather than having to set these up in separate master data tables.

Multiple codes for the same Lookup Field Name are set up by simply inserting more lines with the same Lookup Field Name and defining a unique Code and Description (optional) for each line.

Some master data types have inherent parent-child relationships. A good example of this is the relationship between Commodity Code and Commodity Group Code. Oranges (Commodity Code) fall within a ‘parent’ group (Commodity Group Code) called Citrus. Oranges is certainly not stone fruit or pome fruit.

To support these inherent parent-child relationships a code for a Lookup Field Name can be ‘linked’ to its parent by specifying the Parent Lookup Field Name (this should exist independently as a Lookup Field Name in the same table) and Parent Code.

Additional attributes and relationships between different types of master data can be set up with the use of Extended Lookup Values. For Example: Lookup Field Name: Producer Code = A0010 linked to Extended Lookup Field Name: Production Area = NC (Northern Cape).

## Master data that should be set up in Linc Lookup Values

| Lookup Field Name         | Parent Lookup Field Name |
| ------------------------- | ------------------------ |
| Addendum Class Code       |                          |
| Brand Code                |                          |
| Channel Code              |                          |
| Claim Code                |                          |
| Class Code                |                          |
| Color Code                | Commodity Code           |
| Commercial Invoice Title  |                          |
| Commodity Group Code      |                          |
| Commodity Code            | Commodity Group Code     |
| Compliance Scheme Code    |                          |
| Container Type Code       |                          |
| Country Code              | Region Code              |
| Customer Quality Code     |                          |
| Customs Deduction         |                          |
| Defect Code               |                          |
| Exporter                  |                          |
| Freight Agent Code        |                          |
| Freight Forwarder Code    |                          |
| Freight Point             |                          |
| Freighter Code            | Transport Method         |
| Freighter Trip Code       | Freighter Code           |
| Global Gap Number         |                          |
| Haulier                   |                          |
| Inner Pack Code           |                          |
| Inspection Point          |                          |
| Inspection Status         |                          |
| Market Code               |                          |
| Organisation Code         |                          |
| Outer Pack Code           |                          |
| Packhouse Code            |                          |
| Pallet Base Code          |                          |
| Pallet Height Code        |                          |
| Producer Code             |                          |
| Producer Site Code        | Producer Code            |
| Production Area           |                          |
| Produce Trade Claim Type  |                          |
| Proforma Invoice Title    |                          |
| Quality Grade Code        |                          |
| Quality Inspection Type   |                          |
| Quality Sample Size       |                          |
| Region Code               |                          |
| Rejection Reason Code     |                          |
| Retailer Code             |                          |
| Shipper                   |                          |
| Shipping Temperature Code |                          |
| Size Code                 | Commodity Code           |
| Temptale Type Code        |                          |
| Trade Invoice Title       |                          |
| Trade Cr. Memo Title      |                          |
| Trade Type                |                          |
| Transport Method          |                          |
| Variety Code              | Variety Group Code       |
| Variety Group Code        |                          |
| Warehouse Zone Code       |                          |