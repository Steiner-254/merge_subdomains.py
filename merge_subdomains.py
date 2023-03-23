subdomains = [
    "subdomain1.example.com",
    "subdomain2.example.com",
    "subdomain1.example.com",
    "subdomain3.example.com",
    "subdomain2.example.com",
    "subdomain4.example.com"
]

merged_subdomains = {}
for subdomain in subdomains:
    domain_name = subdomain.split(".")[0]
    if domain_name not in merged_subdomains:
        merged_subdomains[domain_name] = set()
    merged_subdomains[domain_name].add(subdomain)

merged_list = []
for domain_name, subdomains in merged_subdomains.items():
    merged_list.extend(list(subdomains))

print(merged_list)
