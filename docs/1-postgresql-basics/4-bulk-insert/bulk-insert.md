# Bulk Insert in Postgresql
So I have a dataset with some 2 M rows and 17 columns. I used the `COPY` command to 
insert the data from terminal. It took about 52 seconds.

```
COPY business_data(CompanyName,EmailAddress,ContactFullName,ContactJobTitle,PhoneNumber,FaxNumber,Address,Address2,Address3,Town,County,Postcode,Region,Country, SICCode, BusinessCategory,WebAddress) FROM '/home/soumic/Codes/cloud-research-odyssey/files-n-datasets/business_data/input.csv' DELIMITER '*' csv header;
```

The main trouble was cleaning up the data rather than the actual insert. I used a simple java code to remove imcompatible rows.