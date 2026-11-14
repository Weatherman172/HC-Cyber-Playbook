### Portfolio Artifact 1 — Data-to-Decision Playbook

**Course:** Cisco CCNA Security  
**Semester:** Autumn 2026  
**Knowledge Area:** System Security  
**Crosscutting Concepts:** Risk, Systems Thinking, Responsible AI  
**Skills Demonstrated:** Splunk searches, log analysis, threat intelligence, evidence verification, and investigation planning.

#### Overview

During Weeks 3 and 4, I learned how cybersecurity analysts use different security logs and tools to investigate suspicious activity. This playbook is intended for beginner SOC analysts who need to determine
which data to search, what the results mean, and whether additional investigation is necessary.

#### What I Did

I completed several Cisco Networking Academy activities involving Frothly Brewery, threat intelligence, cloud security, and Windows antivirus logs.

In Activity 1.5, I learned how to identify useful data sources for an investigation. In Activity 2.2, I used CyberChef and threat intelligence research to examine suspicious file hashes. This taught me that 
identifying a file associated with malware does not necessarily prove it executed on a computer.

For Milestone 1, I focused on determining whether a suspicious file was only detected or whether there was evidence that it actually ran.

During Week 4, I reviewed cloud security evidence, Splunk searches, and antivirus logs. Activity 4.3 showed how Windows event logs could be filtered to identify antivirus activity on different computers.

#### Evidence

**Security Data Sources**

| Data Source | Useful Information | Limitation |
|---|---|---|
| Authentication logs | Login attempts and account activity | Failed logins do not prove compromise |
| Endpoint logs | Antivirus alerts and process activity | Alerts do not always prove infection |
| Network logs | Connections, ports, and traffic | Connections alone do not explain intent |
| Cloud logs | Resource access and permission changes | Changes may be authorized |

**My Investigation Procedure**

1. Define the security question and time range.
2. Choose the most relevant security logs.
3. Inspect available fields such as host, source, sourcetype, and timestamp.
4. Apply filters and use commands such as `stats` to summarize results.
5. Separate observations from assumptions and identify missing evidence.
6. Compare findings with another source and document or escalate suspicious activity.

**Original Example – Fictional Training Data**

Suppose three computers generated the following Windows events during one hour:

| Computer | All Events | Antivirus Events |
|---|---:|---:|
| PC-01 | 20 | 8 |
| PC-02 | 25 | 3 |
| PC-03 | 10 | 1 |

A broad search would show PC-02 with the most events. However, filtering for antivirus activity would show PC-01 with the most matching events.

An illustrative Splunk search could be:

`index=training sourcetype=WinEventLog source="WinEventLog:Application" SourceName="Symantec AntiVirus" | stats count by host`

This is an example only. The search was not executed, and the index and application field value would need validation.

**Observation:** PC-01 has the most antivirus events.

**Interpretation:** PC-01 may need further investigation, but eight antivirus events do not prove an infection.

**Next Check:** Review the antivirus detection details and compare them with endpoint process activity.

#### AI Use & Verification

I used AI to help organize my notes and explain Splunk search logic.

In my Week 4 query-review exercise, the illustrative AI draft counted all authentication events instead of only failed attempts.

The original logic was:

`stats count by user`

I corrected it to:

`search action="failed" | stats count by user`

I checked the field values against the fictional records and manually counted the failed events. The expected results were one failed event for demo-A and one for demo-B.

The check was manual, and the corrected query was not executed in Splunk. My final judgment was that the corrected logic answered the intended question, but a real investigation would still require an
approved index and time range.

I also revised my explanation of antivirus alerts after reviewing Activity 4.3. I originally focused on which computers had the most alerts, but I learned that event counts alone cannot determine how serious
a threat is.

#### What I Learned

The biggest thing I learned was that finding suspicious activity does not automatically mean an attack occurred. Analysts need to choose the right data sources, understand what the logs show, and verify their
findings.

I also learned that filtering searches incorrectly can produce misleading results. Even a small mistake in a query can change the conclusion.

#### Cybersecurity Connection

These skills help analysts investigate malware, unauthorized access, and suspicious network activity. Comparing multiple sources of evidence supports Defense in Depth and helps prevent incorrect conclusions.

#### Professional Connection

SOC analysts use these methods to investigate alerts, identify affected systems, and document findings for other team members.

This assignment helped me understand the importance of being accurate, checking my work, and explaining what I know versus what still needs to be investigated.

**Sources:** Cisco Networking Academy, *Data and Tools for Defense Analysts*, Activities 1.5, 2.2, 4.1–4.3; Splunk Search Reference (https://help.splunk.com/en/splunk-enterprise/spl-search-reference).
