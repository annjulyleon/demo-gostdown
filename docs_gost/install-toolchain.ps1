###### Hard-coded params ######
$pandoc_version = "2.17.1.1"
$pandoc_crossref_version = "0.3.12.2a"

###### Function definitions ######

function App-Needs-Installation
{
  param (
    [Parameter(Mandatory=$true)][string]$name
  )

  where.exe $name 2>&1 | out-null

  if ($LASTEXITCODE -eq 0) {
    $false
  } else {
    $true
  }
}

function Install-App-By-Name {
  param (
    [Parameter(Mandatory=$true)][string]$name,
    [Parameter(Mandatory=$true)][string]$version
  )

  winget.exe install -v $version $name
}

function Install-App-By-Id {
  param (
    [Parameter(Mandatory=$true)][string]$id
  )

  winget.exe install --id $id
}

function Print-With-Padding {
  param (
    [Parameter(Mandatory=$true)][string]$message
  )

  Write-Host
  Write-Host $message
  Write-Host
}

function Add-Temp-Path {
  param (
    [Parameter(Mandatory=$true)][string]$path
  )

  $env:Path += ";${path}"
}

function Add-Constant-Path {
  param (
    [Parameter(Mandatory=$true)][string]$path
  )

  $old_path = [Environment]::GetEnvironmentVariable('Path')
  [Environment]::SetEnvironmentVariable('Path', "${old_path};${path}", [System.EnvironmentVariableTarget]::User)
}

function Download-And-Extract
{
  param (
    [Parameter(Mandatory=$true)][string]$url
  )

  $temp_archive_path = New-Guid

  Print-With-Padding "Downloading archive into temp file ${temp_archive_path}..."
  Invoke-WebRequest $url -OutFile $temp_archive_path
  
  Print-With-Padding "Extracting files from downloaded archive..."
  7z.exe e $temp_archive_path

  Print-With-Padding "Removing temp archive file..."
  Remove-Item $temp_archive_path
}

###### Command execution starts here ######

if (App-Needs-Installation pandoc) {
  Print-With-Padding "Pandoc is not installed. Installing..."

  Install-App-By-Name pandoc $pandoc_version
  Add-Constant-Path "${env:LOCALAPPDATA}\Pandoc"

  Print-With-Padding "Successfully installed Pandoc"
} else {
  Print-With-Padding "Pandoc is already installed"
}

if (App-Needs-Installation pandoc-crossref) {
  Print-With-Padding "Pandoc-Crossref is not installed. Installing..."

  Add-Temp-Path "C:\Program Files\7-Zip"

  if (App-Needs-Installation 7z) {
    Print-With-Padding "7zip is needed to extract Pandoc-Crossref but it is not installed. Installing..."
    Install-App-By-Id 7zip.7zip
  }

  Download-And-Extract "https://github.com/lierdakil/pandoc-crossref/releases/download/v${pandoc_crossref_version}/pandoc-crossref-Windows.7z"

  Print-With-Padding "Successfully installed Pandoc-Crossref"
} else {
  Print-With-Padding "Pandoc-Crossref is already installed"
}