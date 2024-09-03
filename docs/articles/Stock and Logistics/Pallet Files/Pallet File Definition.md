---
grand_parent: Stock and Logistics
has_children: false
layout: default
nav_order: 31001
parent: Pallet Files
title: Pallet File Definition
---

Pallet File Definition

Multiple **[Pallet File Definitions](https://file+.vscode-resource.vscode-webview.net/Users/attieretief/Github/Linc-ProduceLinc-ghpages/documentation/pallet-file-definition#set-up-a-pallet-file-definition "pallet-file-definition#set-up-a-pallet-file-definition")** can be set up – each with its own set of mapped Pallet File Fields **[Pallet File Fields](https://file+.vscode-resource.vscode-webview.net/Users/attieretief/Github/Linc-ProduceLinc-ghpages/documentation/pallet-file-definition#map-pallet-file-fields "pallet-file-definition#map-pallet-file-fields")**. When pallet files are imported, the system will automatically find the first appropriate pallet file definition that matches the incoming file and use the related field mapping to insert values from the relevant section in the pallet file into the pallet fields in the system. Fields can be mapped to the system from the Body and Header of a pallet file.




The values and/or options in the fields **Fi****le Type, Section Type, Field Deli****miter**, **File Prefix**, **File Prefix Case Sensitive**, **File Suffix** and **File Suffix Case Sensitive** are used to find the matching pallet file definition. **Header Rows**, **Footer Rows** and **Exclude Rows not Starting With** determine which lines in the pallet file are imported.




It is possible to set up a 'generic’ file definition to handle the majority of pallet file processing for a certain file type, eg. PO files, and then create a more specific pallet file definition to deal with cases where the same kind of file from certain sources have a different field mapping. To accomplish this, the system sorts the pallet file definitions in ascending order according to the values in the **Code** field and uses the first 'matching’ file definition for processing the incoming pallet file.




To ensure that the more specific, matching definition is used for a pallet file, the file definitions should thus be set up in such a way that the most generic file definition is the last record when the definitions are sorted in ascending order by **Code**.