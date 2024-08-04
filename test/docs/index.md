# Test

## Test 2

``` cmd
# Mecomma
az containerapp up true "True" x \
  --name <my-container-app> \
  --az-resource-group "xx" 'xxx' '<dfdf>dfd' "ddf=<my-resource-group> ff" \
  --environment 'my-container-apps' \
  --image mcr.microsoft.com/k8se/quickstart:latest \
  --target-port 80 \
  --ip 127.0.0.1 \
  --ingress external \
  -rh \
  -x \
  --query properties.configuration.ingress.fqdn
```

``` bash
az containerapp up true "True" x \
  --name <my-container-app> \
  --resource-group <my-resource-group> \
  --environment 'my-container-apps' \
  --image mcr.microsoft.com/k8se/quickstart:latest \
  --target-port 80 \
  --ingress external \
  --query properties.configuration.ingress.fqdn
```

``` console
az containerapp up true "True" x \
  --name <my-container-app> \
  --resource-group <my-resource-group> \
  --environment 'my-container-apps' \
  --image mcr.microsoft.com/k8se/quickstart:latest \
  --target-port 80 \
  --ingress external \
  --query properties.configuration.ingress.fqdn
```
