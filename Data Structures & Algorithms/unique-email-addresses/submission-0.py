class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seenMail = set()
        for i in emails:
            local, domain = i.split('@')
            local = local.split('+')[0]
            local = local.replace('.','')
            seenMail.add(f"{local}@{domain}")
        return len(seenMail)