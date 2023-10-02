# Metrics Data Dictionary

## Usage and Governance Reporting Categories
**Events:** granular event data
**Membership:** who is part of your account and when
**Resources:** granular inventory of resources
**Tops:** most active users, most frequent searches, etc.
**Visits:** how often is the tool used, by whom

## Time Zone
All dates and timestamps are based on UTC time zone

## Definitions
**API Event:**
* A record in the data corresponding to any action executed by an application or integration that uses data.world's API. 
* [data.world integrations](https://apidocs.data.world/docs/dwapi-spec-stoplight/ZG9jOjIxNTk3MjAw-api)
* [data.world API](https://apidocs.data.world/docs/dwapi-spec-stoplight/ZG9jOjIxNTk3MjAw-api)

**Customer Real Active Day (CRAD):**
* The technical definition of a RAD (Real Active Day):
    * measured at the level of individual users
    * must be a return day (first day on platform is excluded)
    * ui_events + api_events > 10
* We use RADs as a measure of engagement. As compared with a regular "user day," a RAD requires a slightly higher level of engagement (more than 10 distinct events). RADs purport to measure "real" active days by excluding user days with very low volume of interactions with the platform.

**UI Event:**
* A record in the data corresponding to any action executed by a human directly in the data.world app. 
* UI Events occur when a person "clicks" buttons in data.world.

## Notes and Caveats
**data.world Employees:**
* Membership and Visits tables do not contain data.world employees.
* data.world employees may appear in Events, Resources and Tops tables.

**Refresh Schedule:**
* Data in Events and Visits tables is within 24 hours of up-to-date.
* Data in Membership, Resources and Tops is usually within 24 hours of up-to-date, but may be between 24 and 48 hours behind.

**Failed Syncs:** 
* Occasionally, table may fail to sync. A red dot on the table's icon will indicate that the most recent sync failed.
* Attempt to sync the table manually by opening the table and then clicking "sync now" where the table's metadata is displayed in the sidebar on the right. 
* If this does not resolve the problem, then please report in a support ticket. 

## Tables

### Events - Authorization Requests
A record of instances when requests for authorization were submitted

**columns**
1. **date:** The date event occurred
2. **requester:** The unique account ID for the user
3. **requester_email:** The requester's email address
4. **requester_displayname:** The requester's display name
5. **approver:** The approver's agentid
6. **owner:** The resource owner and the namespace where the resource resides. Together with the resource ID (owner/resourceid) this becomes a unique ID, and also used for the web URL to view the resource.
7. **resource:** the resource identifier -- together with the resource owner (owner/resourceid) this becomes a unique ID, and also used for the web URL to view the resource
8. **resourceid:** the unique resource identifier -- concatenation of (owner/resource)$ and also used for the web URL to view the resource
9. **resourcetype:** The type of approved resource
10. **visibility:** The visibility of the resource -- (PUBLIC or PRIVATE)
11. **level:** The level of the granted authorization -- (READ, WRITE or ADMIN)
-----------------------
### Events - Bookmarks
A record of bookmarks created

**columns**
1. **date:** date event occurred
2. **agentid:** The unique account ID for the user.
3. **action:** "bookmark"
4. **owner:** The resource owner and the namespace where the resource resides. Together with the resource ID (owner/resourceid) this becomes a unique ID, and also used for the web URL to view the resource.
5. **resource:** the resource identifier -- together with the resource owner (owner/resourceid) this becomes a unique ID, and also used for the web URL to view the resource
6. **email:** email address associated with user's data.world
-----------------------
###  Events - Create Dataset Project Events
A record of events representing the creation of a dataset or project

**columns**
1. **date:** date event occurred
2. **owner:** The resource owner and the namespace where the resource resides. Together with the resource ID (owner/resourceid) this becomes a unique ID, and also used for the web URL to view the resource.
3. **resource:** the resource identifier -- together with the resource owner (owner/resourceid) this becomes a unique ID, and also used for the web URL to view the resource
4. **resourceid:** the unique resource identifier -- concatenation of (owner/resource)$ and also used for the web URL to view the resource
5. **createdby:** the unique agentid of the user who created the dataset or project
6. **email:** email address associated with dataset or project creator's data.world account
7. **visibility:** PRIVATE, OPEN or DISCOVERABLE
8. **type:** DATASET or PROJECT
------------------------
### Events - Dataset Activity - By Day
A fact table containing dataset activity measurements, aggregated by UTC-based calendar day

**columns**
1. **date:** UTC-based calendar date
2. **owner:** The resource owner and the namespace where the resource resides. Together with the resource ID (owner/resourceid) this becomes a unique ID, and also used for the web URL to view the resource.
3. **resource:** the resource identifier -- together with the resource owner (owner/resourceid) this becomes a unique ID, and also used for the web URL to view the resource
4. **resourceid:** the unique resource identifier -- concatenation of (owner/resource)$ and also used for the web URL to view the resource
5. **queries_run:** count of run query events executed within the dataset
6. **queries_saved:** count of save query events executed within the dataset
7. **downloads:** count of download events executed within the dataset
8. **pageviews:** count of pageviews for the dataset homepage
9. **bookmarks:** count of bookmarks added for the dataset
10. **auth_requests:** count of authorization requests submitted for the dataset
------------------------
### Events - Downloads
A record of events representing the download of a dataset, file or query result

**columns**
1. **date:** the UTC-based calendar date when download occurred
2. **agentid:** The unique account ID for the user
3. **email:** email address associated with user's data.world account
4. **displayname:** user's name
5. **type:** The type of download: dataset, file, query-result, or error-linter (download error)
6. **owner:** The resource owner and the namespace where the resource resides. Together with the resource (owner/resource) this becomes a unique ID, and also used for the web URL to view the resource
7. **resource:** the resource identifier -- together with the resource owner (owner/resource) this becomes a unique ID, and also used for the web URL to view the resource
8. **resourceid:** the unique resource identifier -- concatenation of (owner/resource) and also used for the web URL to view the resource
9. **filename:** name of the downloaded file or query-result
10. **filelabels:** array containing any labels assigned to the file at the time of download event; note that the most recent day's filelabels records may not be completely up-to-date if it's the case that changes or additions were made to a file's labels a short time prior to the download event
------------------------
### Events - Catalog Resources Pages Activity - By Day
A fact table containing catalog pages activity such as views, edits, suggestions and deletes done by agents aggregated by UTC-based calendar day

**columns**
1. **date:** UTC-based calendar date
2. **owner:** the org namespace where catalog resource resides
3. **agentid:** the agentid who took an action (views, edits or suggestions_submitted)
5. **resourcetype:** the catalog resource type
6. **resource:** the catalog resource's unique ID. This represents the unique IRI value of the resource
7. **resourcename:** the name of the catalog resource
8. **views:** count of pageviews by the agent for that resource. When > 0 this represents a resource viewed by an agent
9. **creates:** count of resource created by an agent. When > 0 this represents a new resource created by an agent
10. **edits:** count of edits done to a resource by an agent. When > 0 this represents an edit done to a resource.
11. **suggestions_submitted:** count of suggestions submitted by the agent for that resource.
12. **deletes:** when > 0 this represents a resource deleted by an agent.
-----------------------
### Events - Catalog Resources Approved Or Denied Suggestions - By Day
A fact table containing approvals or denials on suggestions submitted by agents

**columns**
1. **date:** UTC-based calendar date
2. **owner:** the org namespace where catalog resource resides
3. **responder:** the agentid who denied or approved the suggestion submitted
4. **requester:** the agentid who submitted the suggestions
5. **resourcetype:** the catalog resource type
6. **resource:** the catalog resource's unique ID. This represents the unique IRI value of the resource
7. **resourcename:** the name of the catalog resource
8. **suggestions_approved:** when > 0, it represents an approval from the responder to the suggestion submitted by the requester
9. **suggestions_denied:** when > 0, it represents a denial from the responder to the suggestion submitted by the requester
-----------------------
### Events - Catalog Resources Pending Suggestions - By Day
A fact table containing suggestions that have neither been approved or denied.

**columns**
1. **date:** UTC-based calendar date
2. **owner:** the org namespace where catalog resource resides
3. **agentid:** the agentid who submitted the suggestion
4. **resourcetype:** the catalog resource type
5. **resource:** the catalog resource's unique ID. This represents the unique IRI value of the resource
6. **resourcename:** the name of the catalog resource
-----------------------
### Events - Pageviews - Last 90 Days
A record of pageview events, including viewer and resource viewed

**columns**
1. **date:** date event occurred
2. **ts:** Datetime of event in standard ISO 8601 format
3. **agentid:** The unique account ID for the visitor user
4. **action:** "pageview"
5. **urlpath:** ID of the resource viewed
6. **referrer:** The URL path of the web app page that was viewed -- The path is the part of the URL that comes after "https://data.world"
7. **email:** email address associated with user's data.world
---------------------------
### Events - Queries
A detailed log of query events occurring during the past 90 days

**columns**
1. **owner:** the resource owner and the namespace where the resource resides. Together with the resource (owner/resource) this becomes a unique ID, and also used for the web URL to view the resource
2. **ts:** timestamp (UTC timezone)
3. **environment:** internal use only
4. **queryrunagentid:** the unique account ID for the user that executed query
5. **queryruntoken:** unique query run ID
6. **action:** the status of the query. This has values such as `start`, `end` , `cancel` and `error` besides a suite of other in flight query events that start with string `execute`.
7. **resourceid:** the unique resource identifier -- concatenation of (owner/resource) and also used for the web URL to view the resource
8. **origination:** the part of the plaform (api, query ui, preview, etc) that triggered the query
9. **querytext:** original text of the query. should only be included on start, prepare.end & end events
10. **targetquerytext:** contains the SQL that was sent to the downstream system after compilation from dwSQL (snowflake, athena, etc.)
11. **totalquerytime:** time,in milliseconds, for the query to execute (only available on `end` events)
12. **totalresultcount:** total result count for the query (only available on `end` events)
13. **eventid:** unique identifier for the log event itself

Description of **origination** categories:
* **api** means it was kicked off by the public api
* **query** means it came from a query in the UI
* **ping** means it was part of a health check to make sure the service is working
* **null** when none of those match
-------------------------------
### Events - Searches - Last 90 Days
A log of search events during past 90 days

**columns**
1. **date:** calendar data when event occurred
2. **ts:** Datetime of event in standard ISO 8601 format
3. **agentid:** user who executed search event
4. **email:** the email address for the account responsible for executing the search event 
5. **displayname:** the name associated with the account responsible for executing the query event
6. **action:** type of search event
7. **search_value:** search terms the user entered -- if a tag or filter was applied, this will show like "tag:finance" for example
8. **num_results:** The number of search results returned, if applicable to the event action type
9. **selected_facets:** the filters selected and applied in the unified search view

#### Events - Searches - Last 90 Days: action
* **Search Bar Result Click** is when someone clicks an autosuggestion that appears as someone is typing in the search bar in the top header.
* **Search Bar Submit** is typing in the search bar and hitting enter in the header available on every page.
* **Search View Submit** is typing in the search bar on the Search page itself (not in the header) and hitting enter.
* **Search View Search Results** is being displayed a set of results on the search view. Both **Search Bar Submit** and **Search View Submit** result in **Search View Search Results** being triggered. However there are other ways in our app someone can be sent to search results and trigger the **Search View Search Results** event, so the numbers won't line up exactly.
-------------------------------------------
### Events - Dataset or Project Views By Org
Ranked list of number of dataset or project views by org

**columns**
1. **org:** org ID
2. **views:** count of dataset or project views
---------------------------------------------
### Membership - All Time List
A simple Roster of all current and past members (includes orgs)

**columns**
1. **agentid:** The unique account ID for the visitor user
2. **email:** email address of the user -- if DELETED, user no longer exists on data.world
3. **displayname:** display name of the user -- if DELETED, user no longer exists on data.world
4. **current_member:** (boolean) TRUE: the user account is currently and actively on record; FALSE: the user account has been removed
5. **last_date_active:** The most recent date that the user was active on data.world
--------------------------
### Membership - By Date
A granular listing of membership by date

**columns**
1. **date:** calendar date of membership
2. **agentid:** the unique account ID for the member
3. **email:** the member's email address
4. **displayname:** the member's name
---------------------------------------------------
### Membership - Current
A detailed roster of all current members

**columns**
1. **displayname:** user's name
2. **agentid:** user ID
3. **email:** email address
4. **startdate:** calendar date user first visited platform
5. **lastseen:** calendar date of user's most recent activity (either via UI or via API)
6. **onboard_date:** calendar date user completed enrollment
7. **api_events:** number of api events executed by user
8. **ui_events:** number of ui events executed by user
9. **pageviews:** number of resources viewed by user
10. **queries_created:** number of queries created by user
11. **datasets_created:** number of datasets created by user
12. **projects_created:** number of projects created by user
13. **downloads:** number of times user downloaded a file or dataset
-------------------------------------------------
### Membership - Current By Org
A granular listing of membership, broken down by org

**columns**
1. **agentid:** the unique account ID for the member
2. **displayname:** the member's name
3. **email:** the member's email address
4. **org:** the org that the user is a member of
5. **auth_level:** the org-level authorization granted to member (READ, WRITE or ADMIN)
6. **visibility:** the member's org-level visibility setting (PRIVATE or PUBLIC)
7. **date_auth_updated:** the date of most recent update to member's org-level authorization settings
8. **startdate:** calendar date member first visited platform
9. **lastseen:** calendar date of member's most recent visit
---------------------------------------------------
### Membership - Daily
Daily count of total number of members in customer org

**columns**
1. **date:** the calendar date
2. **members:** number of members in customer org
-------------------------------------------------------
### Resources - Authorizations
A listing of all authorizations

**columns**  
1. **date:** the calendar date authorization when was granted
2. **party** the agent or group who was granted authorization
3. **partyid:** the unique ID of the user or group that was granted authorization
4. **partytype** the party type that requested the authorization (e.g. agent, group)
5. **level:** the level of authorization that was granted. e.g. ADMIN, READ or WRITE
6. **resource:** the resource on which the authorization was granted
7. **resourceid:** the id of the resource
8. **resourcetype:** the type of the resource. for e.g. org, group, allCatalogs, dataLibrary, datasets, etc.
9. **owner:** org namespace in which the resource lives or belongs to
10. **visibility:** the visibility level applied to resource
11. **requesterparty** the user account that requested the authorization
12. **approverparty:** the user account that approved the authorization
----------------------------------------------------------
### Resources - Comments
A log of all comment events that took place in customer org

**columns**
1. **agentid:** unique ID of user that posted comment
2. **owner:** the resource owner and the namespace where the resource resides -- together with the resource (owner/resource) this becomes a unique resourceID, and also used for the web URL to view the resource
3. **resource:** the resource identifier -- together with the resource owner (owner/resourceid) this becomes a unique ID, and also used for the web URL to view the resource
4. **resourceid:** the unique resource identifier -- concatenation of (owner/resource)$ and also used for the web URL to view the resource
5. **resourcetype:** type of resource in which comment occurred ("dataset", "table" or "datasetinsight")
6. **created_date:** the calendar date when the comment was posted
------------------------------------------------
### Resources - Database Connections
A listing of all existing database connections

**columns**
1. **owner:** the unique ID of the individual or org that owns the connection
2. **database_connection_label:** name given to connection by creator of connection
3. **database_connection_type:** type of database connection (eg, Snowflake, PostgresSQL, etc.)
4. **connection_agentid:** ID of user that created connection
5. **connection_agent_displayname:** name of user that created connection
6. **connection_created:** calendar date when connection was created
7. **connection_updated:** calendar date when connection was last updated
8. **connection_updatedby:** agentid of user that last updated connected
-----------------------------------------
### Resources - Dataset Owner Report
A summary table of dataset metrics by owner and datasetid

**columns**
1. **owner:** the resource owner and the namespace where the resource resides -- together with the resource (owner/resource) this becomes a unique resourceID, and also used for the web URL to view the resource
2. **resource:** the resource identifier -- together with the resource owner (owner/resourceid) this becomes a unique ID, and also used for the web URL to view the resource
3. **resourceid:** the unique resource identifier -- concatenation of (owner/resource)$ and also used for the web URL to view the resource
4. **queries_run:** count of query runs
5. **queries_saved:** count of queries saved
6. **downloads:** count of downloads
7. **pageviews:** count of number of times dataset/project was viewed
8. **bookmarks:** count of number of times dataset/project was bookmarked
9. **auth_requests:** count of auth requests placed on dataset/project
------------------------------------------------
### Resources - Datasets
A detailed listing of all (currently existing) datasets

**columns**
1. **owner:** the resource owner and the namespace where the resource resides -- together with the resource (owner/resource) this becomes a unique resourceID, and also used for the web URL to view the resource
2. **resource:** the resource identifier -- together with the resource owner (owner/resourceid) this becomes a unique ID, and also used for the web URL to view the resource
3. **resourceid:** the unique resource identifier -- concatenation of (owner/resource)$ and also used for the web URL to view the resource
4. **description:** the description associated with the dataset/project
5. **summary:** the contents of the "summary" markdown field
6. **createdby_agentid:** the user ID of the dataset creator
7. **createdby_email:** the email of user that created dataset
8. **createdby_displayname:** the name of user that created dataset
9. **createdby_client:** the type of client: "user-client" or "admin-client"
10. **created:** the calendar date when dataset was created
11. **updated:** the calendar date when dataset was last updated
12. **visibility:** the access level the dataset is set to: "PRIVATE", "DISCOVERABLE" or "OPEN"
13. **tags:** current list of tags added to the dataset
14. **notificationsEmail:** email addresses associated with the notifications for the dataset;
---------------------------------------------------
### Resources - Dataset Files
A detailed listing of all (currently existing) files residing in datasets

**columns**
1. **owner:** The resource owner and the namespace where the resource resides. Together with the resource (owner/resource) this becomes a unique ID, and also used for the web URL to view the resource
2. **resource:** the resource identifier -- together with the resource owner (owner/resource) this becomes a unique ID, and also used for the web URL to view the resource
3. **resourceid:** the unique resource identifier -- concatenation of (owner/resource) and also used for the web URL to view the resource
4. **dataset_name:** the dataset's name
5. **file_name:** the file's name
6. **file_created_time:** the UTC date:time when file created
7. **file_created_date:** the UTC date when file was created
8. **file_createdby_client:** the client used to create the dataset -- useful for distinguishing API- from UI-based events
9. **file_materialized_or_virtualized:** file type (MATERIALIZED or VIRTUALIZED)
10. **is_file_discoverable:** is the mark as preview setting enabled for this file (boolean)
11. **file_size_in_bytes:** file size (in bytes)
---------------------------------------------------
### Resources - Followers
A list of followers of users or orgs

**columns**
1. **following:** ID of individual or org that is followed
2. **agentid:** ID of individual follower
3. **created:** Calendar date when follow event occurred
4. **displayname:** name of individual follower
5. **email:** email address of individual follower
6. **company:** follower's company as represented in follower's profile
7. **bio:** follower's bio as represented in follower's profile
-----------------------------------------------------
### Resources - Insights
A listing of all (currently existing) project insights

**columns**
1. **createdby:** agentid of user that created insight
2. **owner:** the resource owner and the namespace where the resource resides -- together with the resource (owner/resource) this becomes a unique resourceID, and also used for the web URL to view the resource
3. **resource:** the resource identifier -- together with the resource owner (owner/resourceid) this becomes a unique ID, and also used for the web URL to view the resource
4. **resourceid:** the unique resource identifier -- concatenation of (owner/resource)$ and also used for the web URL to view the resource
5. **created_date:** calendar date when insight was created
--------------------------------------------------
### Resources - Live Metadata Assets Created - By Day
A long form series of counts of metadata assets created by date

**columns**
1. **date:** UTC-based calendar day
2. **owner:** the org where the asset resides
3. **asset:** metadata asset type
4. **live_assets_created:** number of live metadata assets created on the calendar day 
5. **total_assets_created:** number of total (live or staged) metadata assets created on the calendar day
6. **cumulative_live_assets:** the cumulative total number of live assets 
7. **cumulative_total_assets:** the cumulative total number of total assets (including live and staged but not live)
--------------------------------------------------
### Resources - Orgs
A detailed list of all orgs owned by customer

**columns**
1. **orgname:** unique ID of org
2. **displayname:** name of org
2. **created:** calendar date when org was created
4. **createdby:** unique agentid of user that created org
5. **updated:** calendar date when org was last updated
6. **updatedby:** unique agentid of user that last updated org settings
7. **website:** website associated with org's profile
8. **bio:** description of org
9. **allowedroles:** roles authorized to use org
-------------------------------------------------
### Resources - Projects
A detailed listing of all (currently existing) projects

**columns**
1. **owner:** the resource owner and the namespace where the resource resides -- together with the resource (owner/resource) this becomes a unique resourceID, and also used for the web URL to view the resource
2. **resource:** the resource identifier -- together with the resource owner (owner/resourceid) this becomes a unique ID, and also used for the web URL to view the resource
3. **resourceid:** the unique resource identifier -- concatenation of (owner/resource)$ and also used for the web URL to view the resource
4. **description:** the description associated with the project/project
5. **summary:** the contents of the "summary" markdown field
6. **createdby_agentid:** the user ID of the project creator
7. **createdby_email:** the email of user that created project
8. **createdby_displayname:** the name of user that created project
9. **createdby_client:** the type of client: "user-client" or "admin-client"
10. **created:** the calendar date when project was created
11. **updated:** the calendar date when project was last updated
12. **visibility:** the access level the project is set to: "PRIVATE", "DISCOVERABLE" or "OPEN"
13. **tags:** current list of tags added to the project
14. **notificationsEmail:** email addresses associated with the notifications for the project
---------------------------------------------------
### Resources - Queries
A detailed list of currently existing queries

**columns**
1. **query_name:** name given to query
2. **querytype:** type of query: "SQL" or "SPARQL"
3. **createdby:** ID of user that created the query
4. **resourcetype:** type of resource where query was created
5. **owner:** the resource owner and the namespace where the resource resides -- together with the resource (owner/resource) this becomes a unique resourceID, and also used for the web URL to view the resource
6. **resource:** the resource identifier -- together with the resource owner (owner/resourceid) this becomes a unique ID, and also used for the web URL to view the resource
7. **resourceid:** the unique resource identifier -- concatenation of (owner/resource)$ and also used for the web URL to view the resource
8. **created_date** the calendar date when query was created
-------------------------------------------------------
### Resources - Snapshot Open Datasets Projects
A count of total number of datasets and projects as well as proportion that are set to open or discoverable

**columns**
1. **n_datasets_projects:** number of currently existing datasets or projects
2. **n_open:** number of currently existing open datasets or projects
3. **n_discoverable:** number of currently existing discoverable datasets or projects
4. **pct_open:** percent of datasets or projects which are open
5. **pct_discoverable:** percent of datasets or projects which are discoverable
6. **pct_open_or_disc:** percent of datasets or projects which are open or discoverable
-----------------------------------------
### Resources - Synced Datasets
A detailed list of all datasets set to sync from source on a schedule

**columns**
1. **owner:** the resource owner and the namespace where the resource resides -- together with the resource (owner/resource) this becomes a unique resourceID, and also used for the web URL to view the resource
2. **resource:** the resource identifier -- together with the resource owner (owner/resourceid) this becomes a unique ID, and also used for the web URL to view the resource
3. **resourceid:** the unique resource identifier -- concatenation of (owner/resource)$ and also used for the web URL to view the resource
4. **connection_agentid:** agentid associated with the connection
5. **connection_created:** calendar date when connection was created
6. **connection_updated:** calendar date when connection was last updated
7. **syncstatus:** status of connection
8. **lastsyncstart:** timestamp of start of most recent sync
9. **lastsyncfinish:** timestamp of finish of most recent sync
10. **nextscheduledsync:** timestamp of next scheduled sync
11. **nextscheduledsynctype:** type of next scheduled sync
----------------------------------------------
### Tops - Bookmarks
A list of the top ten users ranked by number of bookmarks added (by the user)

**columns**
1. **agentid:** ID of the user that executed the action
2. **displayname:** the name of the user that executed the action
3. **email:** email address associated with user's data.world account
4. **bookmarks:** number of bookmarks added
-----------------------------------------
### Tops - Dataset Project Creation
A list of the top ten users ranked by number of datasets created (by the user)

**columns**
1. **agentid:** ID of the user that executed the action
2. **displayname:** the name of the user that executed the action
3. **email:** email address associated with user's data.world account
4. **datasets_created:** number of bookmarks added
-----------------------------------------------
### Tops - Engagement
A list of users ranked by key engagement metrics

**columns**
1. **agentid:** user's unique ID
2. **email:** email address associated with user's data.world account
3. **displayname:** user's name
4. **onboard_date:** date when user's data.world account was created
5. **rads:** count of total all-time Real Active Days (RADs)
6. **ui_events:** count total all-time UI events (clicks in data.world app)
7. **api_events:** count of total all_time events executed using an API client
8. **first_seen:** date of user's first activity in data.world
9. **last_seen:** date user's most recent activity in data.world
-----------------------------------------------
### Tops - Most Bookmarked Resources
A list of datasets/projects, ranked by number of (currently existing) bookmarks

**columns**
1. **owner:** the resource owner and the namespace where the resource resides -- together with the resource (owner/resource) this becomes a unique resourceID, and also used for the web URL to view the resource
2. **resource:** the resource identifier -- together with the resource owner (owner/resourceid) this becomes a unique ID, and also used for the web URL to view the resource
3. **resourcetype:** type of resource that was bookmarked
4. **bookmarks:** count of number currently existing bookmarks
-----------------------------------------------------
### Tops - Most Comments - All Time
A list of resources, ranked by number of times viewed

**columns**
1. **resourcetype:** type of resource where comments were posted
2. **owner:** the resource owner and the namespace where the resource resides -- together with the resource (owner/resource) this becomes a unique resourceID, and also used for the web URL to view the resource
3. **resource:** the resource identifier -- together with the resource owner (owner/resourceid) this becomes a unique ID, and also used for the web URL to view the resource
4. **resourceid:** the unique resource identifier -- concatenation of (owner/resource)$ and also used for the web URL to view the resource
5. **comments:** number of comments posted in resource
------------------------------------------------
### Tops - Most Searched Terms
A ranked list of the most commonly-searched-for terms along with a count of number of occurrences

**Note**: a blank search_value indicates that the user pressed the space bar and then enter -- in other words, submitted a string comprising one or more spaces to the search bar. 

**columns**
1. **search_value:** the searched-for term or phrase
2. **search_type:** the type of search event (see category definitions below)
3. **n:** the number of times the search value and type have been entered into the search bar

**search_type category definitions**
1. **search bar full search:** is counted when a search value is typed into the main search bar and enter is pressed
2. **search results view:** is counted when the search results from full search loads and is viewable to the user 
3. **search bar suggestion click:** is counted when the user types in the main search bar and clicks directly on a suggestion surfaced in the drop down list 
4. **library view:** is counted when a search value is provided and enter pressed in the "Your datasets" view 
5. **glossary view:** is counted when a search value is provided and enter pressed in the Glossary view
6. **data catalog view:** is counted when a search value is provided and enter pressed in the Resources view
7. **analysis hub view:** is counted when a search value is provided and enter pressed in the "Your projects" view
8. **bookmarks view:** is counted when a search value is provided and enter pressed in the Bookmarks view
---------------------------
### Tops - Most Viewed Resources
A list of resources, ranked by number of times viewed

**columns**
1. **owner:** the resource owner and the namespace where the resource resides -- together with the resource (owner/resource) this becomes a unique resourceID, and also used for the web URL to view the resource
2. **resource:** the resource identifier -- together with the resource owner (owner/resourceid) this becomes a unique ID, and also used for the web URL to view the resource
3. **resourceid:** the unique resource identifier -- concatenation of (owner/resource)$ and also used for the web URL to view the resource
4. **resource_type:** type of resource that was viewed: "dataset_or_project," "source," "analysis" or "catalog"
5. **views:** count of number of times the resource has been viewed
------------------------------------------------------
### Tops - Pageviews By Resource and Agentid
Counts of pageviews grouped by viewer and resource viewed

**columns**
1. **viewer:** user who viewed the resource
2. **owner:** the resource owner and the namespace where the resource resides -- together with the resource (owner/resource) this becomes a unique resourceID, and also used for the web URL to view the resource
3. **resource:** the resource identifier -- together with the resource owner (owner/resourceid) this becomes a unique ID, and also used for the web URL to view the resource
4. **resourceid:** the unique resource identifier -- concatenation of (owner/resource)$ and also used for the web URL to view the resource
5. **resource_type:** type of resource that was viewed: "dataset_or_project," "source," "analysis" or "catalog"
6. **pageviews:** number of times the user viewed the resource
--------------------------------
### Tops - Most Requested Resources
List of top resources, ranked by number of requests made (against the resource)

**columns**
1. **owner:** The resource owner and the namespace where the resource resides. Together with the resource (owner/resource) this becomes a unique ID, and also used for the web URL to view the resource
2. **resource:** the resource identifier -- together with the resource owner (owner/resource) this becomes a unique ID, and also used for the web URL to view the resource
3. **resourceid:** the unique resource identifier -- concatenation of (owner/resource) and also used for the web URL to view the resource
4. **resource_type:** the type of resource
5. **requests:** number of requests submitted against resourceß
----------------------------------------------
### Visits - Adoption - Daily
A daily summary of number of users who used the platform with proportion which were new users

**columns**
1. **date:** calendar date being summarized
2. **user_days:** Members of the account that are unique visitors that day (at least 1 pageview event).
3. **return_days:** Members of the account that are unique return visitors that day (at least 1 pageview event) and this is not their first day (e.g. creation day).
4. **new_days:** count of users visiting within their first calendar day
5. **percent_new:** new_days / user_days * 100
6. **rads:** count of Real Active Days
7. **percent_rad:** rads / user_days * 100
---------------------------------------------
### Visits - Avg Visits Weekly
Measures the mean number of days (per week) that active users visited the platform.
In other words, for those users who visited the platform at least once during the week,
how many different days, on average, did the users visit?

**column**
1. **week:** calendar week being summarized
2. **weekly_user_days:** number of user days per week
3. **unique_visitors:** number of distict visitors per week
4. **avg_visits_per_week:** average number of distinct days that users visited the platform (during the summarized week)
-------------------------------------------
### Visits - CRADs By Agentid By Day
Listing of Customer Real Active Days (CRAD) by date and agentid

**column**
1. **date:** calendar date
2. **agentid:** unique ID of user who performed CRAD
3. **ui_events:** count of ui_events (clicks in app)
4. **api_events:** count of api_events
-----------------------------------------------
### Visits - CRADs By Day
Counts of Customer Real Active Days (CRAD) grouped by calendar date

**column**
1. **date:** calendar date
2. **rads:** count of Real Active Days per date
-------------------------------------------
### Visits - New Users By Month
Count of new users, summarized by month

**columns**
1. **month:** calendar month being summarized
2. **count:** number of new users during summarized month
----------------------------------------------------
### Visits - Request Rates By Month
A by-month summary of ratio of distinct requesters and total distinct users

**columns**
1. **month:** the month being summarized
2. **unique_visitors:** number of distinct users during the month
3. **unique_requesters:** number of distinct users that made a request for authorization during the month
4. **pct_made_request:** percent of users that made a request during the month
------------------------------------
### Visits - Return Visitor Days
A log of of all past user days, excluding new days (first day on platform)

**columns**
1. **date:** calendar date of return day
2. **agentid:** ID of visiting user
3. **email:** email of visiting user
4. **displayname:** name of visiting user
-------------------------------------------------
### Visits - Return Visitors - All Time List
A list of all users that have visited the platform on at least two separate calendar days.
Includes a count of total number of return days per user.

**columns**
1. **agentid:** ID of visiting user
2. **email:** email of visiting user
3. **displayname:** name of visiting user
4. **return_days:** count of active days (excluding user's first day on platform)
----------------------------------------
### Visits - Return Visitors - Daily
A daily summary showing number of users that visited the platform (excludes first visit calendar day)

**columns**
1. **date:** the calendar date being summarized
2. **return_visitors:** number of users that visited platform (excludes first visit calendar day)
-----------------------------------------
### Visits -- Return Visitors - Monthly
A monthly summary showing number of users that visited the platform (excludes first visit calendar day)

**columns**
1. **month:** the calendar month being summarized
2. **return_visitors:** number of users that visited platform (excludes first visit calendar day)
-------------------------------------
### Visits - Return Visitors - Quarterly
A quarterly summary showing number of users that visited the platform (excludes first visit calendar day)

**columns**
1. **quarter:** the quarter being summarized
2. **return_visitors:** number of users that visited platform (excludes first visit calendar day)
------------------------------------
### Visits - Return Visitors - To Date
Total number of users that have visited the platform on at least two separate calendar days

**columns**
1. **count:** Total number of users that have visited the platform on at least two separate calendar days
--------------------------------------
### Visits - Return Visitors - Weekly
A weekly summary showing number of users that visited the platform (excludes first visit calendar day)

**columns**
1. **week:** the calendar week being summarized
2. **return_visitors:** number of users that visited platform (excludes first visit calendar day)
----------------------------------------
### Visits - Snapshot Repeat Visitors
Shows count of all users that have visited the platform along with the proportion that visited again on a subsequent day

**columns**
1. **all_visitors:** total number of users that visited the platform
2. **return_visitors:** total number of users that visited the platform on at least two separate calendar days
3. **pct_returned:** return_visitors / all_visitors * 100
---------------------------------------
### Visits - Unique Visitor Days
A log of of all past user days

**columns**
1. **date:** the calendar date when the user visited the platform
2. **agentid:** the ID of the visiting user
3. **email:** the email of the visiting user
4. **displayname:** the name of the visiting user
---------------------------------------
### Visits - Unique Visitors - All Time List
A list of all users that have visited the platform.
Includes a count of total number of return days per user.

**columns**
1. **agentid:** ID of visiting user
2. **email:** email of visiting user
3. **displayname:** name of visiting user
4. **unique_days:** number of distinct calendar days when user visited
---------------------------------------
### Visits - Unique Visitors - Daily

A daily summary showing number of users that visited the platform

**columns**
1. **date:** the calendar date being summarized
2. **unique_visitors:** number of users that visited platform
---------------------------------------
### Visits - Unique Visitors - Monthly
A monthly summary showing number of users that visited the platform

**columns**
1. **month:** the calendar month being summarized
2. **unique_visitors:** number of users that visited platform
--------------------------------------
### Visits - Unique Visitors - Quarterly
A quarterly summary showing number of users that visited the platform

**columns**
1. **quarter:** the quarter being summarized
2. **unique_visitors:** number of users that visited platform
--------------------------------------
### Visits - Unique Visitors - To Date
Total number of users that have visited the platform

**columns**
1. **count:** Total number of users that have visited the platform
---------------------------------
### Visits - Unique Visitors - Weekly
A weekly summary showing number of users that visited the platform

**columns**
1. **week:** the calendar week being summarized
2. **unique_visitors:** number of distinct users that visited platform
----------------------------------------
