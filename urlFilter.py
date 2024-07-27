#!/usr/bin/env python3

from argparse import ArgumentParser, FileType
from urllib.parse import urlparse, parse_qs, urlencode

unique_endpoints = [
    "accelerate", "acquire", "activate", "adapt", "add", "adjust", "admin", "alert", "annotate", "anticipate", 
    "apply", "arrange", "build", "calculate", "change", "claim", "collect", "comm", "communicate", "compare", 
    "complete", "compose", "compute", "consolidate", "construct", "contact", "create", "crush", "damage", "def", 
    "define", "del", "deliver", "demo", "demonstrate", "dequeue", "deregister", "derive", "design", "destroy", 
    "detect", "dev", "develop", "devise", "disable", "display", "divide", "dofor", "download", "enable", "explode", 
    "fabricate", "fashion", "forge", "form", "generate", "get", "go", "group", "improve", "inform", "inquiry", 
    "interpret", "kill", "level", "link", "list", "make", "map", "mod", "multiply", "originate", "picture", "post", 
    "preserve", "produce", "promote", "put", "queue", "quit", "reactivate", "read", "recite", "record", "register", 
    "remove", "restore", "restrict", "retrieve", "run", "select", "set", "setup", "show", "sleep", "split", "start", 
    "stop", "study", "sub", "terminate", "test", "understand", "undo", "unqueue", "update", "upload", "upset", 
    "validate", "verify", "com", "latest", "recursive", "ads", "announcements", "api", "api-docs", "apidocs", 
    "auth", "guest", "login", "logout", "batch", "branches", "brands", "call", "campaign", "cart", "categories", 
    "check", "checkin", "clients", "config", "contents", "csp_report", "custom", "customer", "api-doc", "docs", 
    "domains", "events", "geo", "graphql", "identity", "envelope", "init", "insights", "info", "jobs", "jsonpcallback", 
    "jsonws", "invoke", "links", "log", "menus", "models", "modules", "navigation", "notifications", "pages", 
    "permission", "ping", "details", "profile", "properties", "proxy", "rest", "saves", "suggestions", "servers", 
    "server_status", "sessions", "settings", "snapshots", "status", "stores", "subscriptions", "swagger", "index", 
    "token", "tracking", "current", "me", "accounts", "summaries", "ticket", "permissions", "user", "useraccountassignments", 
    "assets", "delete", "userpreferences", "resend-verification", "users", "password", "asset", "filters", "products", 
    "category", "connections", "preferences", "consents", "countries", "devices", "devicetypes", "manufacturers", "order", 
    "userassets", "nexstar", "event", "geoip", "guides", "health", "history", "languages", "address-check", "news", 
    "plugin", "posts", "session", "setting", "stat", "track", "visits", "bid", "collector", "displays", "page", "pub", 
    "spans", "tickets", "groups", "projects", "videos", "view", "whoami", "widget", "doc", "swagger-resources", 
    "activitylogs", "applications", "button", "cookiesync", "identify", "impress", "metric", "open", "pageview", 
    "recentviews", "redirect", "self", "sync", "usersync", "xhr", "resources", "url", "actors", "data", "quote", 
    "metrics", "integrations", "storefront", "widgets", "client", "adx", "iframe", "pageload", "paymentform", "prebid", 
    "stats", "control", "tracker", "undefined", "search", "message", "script", "optimize", "items", "access-token", 
    "account", "amount", "balance", "balances", "bar", "baz", "bio", "bios", "channel", "chart", "circular", "company", 
    "content", "contract", "coordinate", "credentials", "creds", "customers", "dir", "directory", "dob", "email", 
    "employee", "favorite", "feed", "foo", "github", "gmail", "image", "item", "job", "location", "logins", "logs", 
    "member", "members", "messages", "money", "my", "name", "names", "option", "options", "pass", "passwords", "phone", 
    "pin", "prod", "production", "profiles", "publication", "sale", "sales", "site", "theme", "tokens", "twitter", 
    "union", "username", "vendor", "vendors", "version", "website", "work", "yahoo"
]

def extract_components(url):
    parsed_url = urlparse(url)
    root_url = f"{parsed_url.scheme}://{parsed_url.netloc}/"
    path_components = parsed_url.path.strip('/').split('/')

    if "api" in parsed_url.netloc or "api" in path_components:
        return url

    if path_components[-1] in unique_endpoints:
        return url

    if len(path_components) > 1:
        first_directory = path_components[0]
        subdirectories = path_components[1:]
    else:
        first_directory = path_components[0]
        subdirectories = []

    query_params = parse_qs(parsed_url.query)
    query_param_names = sorted(query_params.keys())

    #return (root_url, first_directory, len(subdirectories), tuple(subdirectories), tuple(query_param_names))
    return (root_url, first_directory, len(subdirectories), tuple(query_param_names))

parser = ArgumentParser(prog="urlFilter.py", description="I filter a list of urls")
parser.add_argument("inputfile", help="Input file location", type=str)
parser.add_argument("outputfile", help="Output file location", type=str)
args = parser.parse_args()

seen = set()
counter = 0
filtered_urls = []

with open(args.inputfile) as infile:
    for line in infile:
        url = line.strip()
        counter += 1

        components = extract_components(url)
        if components not in seen:
            seen.add(components)
            filtered_urls.append(url)

with open(args.outputfile, "w") as outfile:
    for f in filtered_urls:
        outfile.write(f"{f}\n")

print(f"Reduced urls from {counter} to {len(filtered_urls)}")
