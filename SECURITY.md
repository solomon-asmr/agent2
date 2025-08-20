# Security Guidelines

This document outlines security best practices for the Agent2 project to ensure sensitive information is protected.

## 🔒 Security Requirements

### API Keys and Credentials

- **Never commit API keys, tokens, or credentials to version control**
- Use environment variables or secure configuration files for all sensitive data
- Rotate API keys regularly
- Use different keys for development, staging, and production environments

### Environment Files

- All `.env` files are automatically excluded from git via `.gitignore`
- Use the provided `.env.example` templates to create your local `.env` files
- Ensure production credentials are managed through your deployment platform's environment variable system

### Configuration Files

- The `config.js` file contains environment-specific URLs and settings
- Never commit environment-specific `config.js` files with production URLs
- Use `config.example.js` as a template for new environments

## 🚨 What NOT to Commit

### ❌ Never commit these files:

- `.env` files (any environment)
- `config.js` files with real URLs/secrets
- Database files with real data
- Session files with user data
- Any file containing:
  - API keys (starts with `AIza...` for Google APIs)
  - Project IDs (format: `project-name-123456-x1`)
  - Authentication tokens
  - Database credentials
  - URLs with embedded secrets

### ✅ Safe to commit:

- `.env.example` template files
- `config.example.js` template files
- Documentation files
- Source code without hardcoded secrets
- Empty database schemas

## 🛡️ Security Checklist Before Committing

Before pushing any code, verify:

- [ ] No API keys in source code
- [ ] No hardcoded URLs with sensitive domains
- [ ] No database files with real data
- [ ] All sensitive configurations use environment variables
- [ ] `.gitignore` includes all sensitive file patterns
- [ ] Configuration templates are provided for new environments

## 🔍 Sensitive Data Patterns to Avoid

Watch out for these patterns in your code:

```bash
# Don't commit these patterns:
AIza[A-Za-z0-9_-]{35}                    # Google API keys
[a-z]+-[a-z]+-[0-9]+-[a-z0-9]+          # GCP Project IDs
sk-[a-zA-Z0-9]{48}                       # OpenAI API keys
xoxb-[0-9]+-[0-9]+-[0-9]+-[a-z0-9]+     # Slack tokens
```

## 🚀 Production Deployment Security

### Environment Variables

Set these environment variables in your production platform:

- `GEMINI_API_KEY`
- `GOOGLE_API_KEY`
- `GCP_PROJECT_ID`
- `GOOGLE_CLOUD_PROJECT`
- `GOOGLE_CLOUD_LOCATION`

### Domain Configuration

- Update all localhost URLs to your production domains
- Use HTTPS for all production URLs
- Use WSS for production WebSocket connections
- Implement proper CORS policies

### Additional Security Measures

- Enable API key restrictions in Google Cloud Console
- Use service accounts with minimal required permissions
- Implement rate limiting on your APIs
- Enable logging and monitoring for suspicious activities
- Keep dependencies updated

## 🔧 Local Development Security

### Safe Practices:

- Use separate API keys for development
- Don't share your local `.env` files
- Regularly rotate development API keys
- Use localhost URLs only for local development

### Testing:

- Use test data only in development
- Don't use production credentials for testing
- Clean up test data regularly

## 📞 Security Incident Response

If you accidentally commit sensitive data:

1. **Immediately rotate the exposed credentials**
2. Remove the sensitive data from git history:
   ```bash
   git filter-branch --force --index-filter \
   'git rm --cached --ignore-unmatch path/to/sensitive/file' \
   --prune-empty --tag-name-filter cat -- --all
   ```
3. Force push to remove from remote:
   ```bash
   git push --force --all
   ```
4. Update all team members about the credential rotation

## 📚 Additional Resources

- [Google Cloud Security Best Practices](https://cloud.google.com/security/best-practices)
- [API Key Security Guidelines](https://cloud.google.com/docs/authentication/api-keys)
- [Git Security Best Practices](https://docs.github.com/en/code-security/getting-started/securing-your-repository)

---

**Remember**: Security is everyone's responsibility. When in doubt, ask for a security review before committing sensitive changes.
