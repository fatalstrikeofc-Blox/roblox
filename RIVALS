-- ╔══════════════════════════════════════════════════════════════╗
-- ║                    RIVALS BLOX HACK                        ║
-- ║                  Professional ESP & Aimbot                   ║
-- ╚══════════════════════════════════════════════════════════════╝

-- Services
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local UserInputService = game:GetService("UserInputService")
local TweenService = game:GetService("TweenService")
local Camera = workspace.CurrentCamera
local LocalPlayer = Players.LocalPlayer

-- Core Variables
local ESPObjects = {}
local Connections = {}
local Mouse = LocalPlayer:GetMouse()



-- Settings
local Settings = {
    ESP = {
        Enabled = true,
        Box = true,
        BoxColor = Color3.fromRGB(255, 255, 255),
        BoxThickness = 2,
        
        Line = true,
        LineColor = Color3.fromRGB(0, 255, 0),
        LineThickness = 2,
        
        Distance = true,
        DistanceColor = Color3.fromRGB(255, 255, 0),
        
        Health = true,
        HealthColor = Color3.fromRGB(0, 255, 0),
        
        Name = true,
        NameColor = Color3.fromRGB(255, 255, 255),
        
        MaxDistance = 500,
        TeamCheck = false
    },
    
    Aimbot = {
        Enabled = true,
        FOV = 100,
        Smoothness = 5,
        VisibilityCheck = true,
        TeamCheck = false,
        MouseButton = Enum.UserInputType.MouseButton2,
        MaxDistance = 300,
        ShowFOV = true,
        TargetPart = "Head", -- "Head" ou "Chest"
        WallhackAimbot = false -- Atirar através da parede
    },
    
    Misc = {
        ModofodaseEnabled = false,
        SpeedHack = false,
        SpeedMultiplier = 3,
        AutoAim = false,
        Wallhack = false,
        AutoExecute = true, -- Nova configuração para auto-execução
        StreamMode = false -- Modo stealth para transmissões
    },
    
    Menu = {
        Visible = true,
        ToggleKey = Enum.KeyCode.Insert,
        Size = UDim2.new(0, 400, 0, 550),
        Position = UDim2.new(0.5, -200, 0.5, -275)
    }
}

-- GUI Creation
local ScreenGui = Instance.new("ScreenGui")
ScreenGui.Name = "RIVALSBloxHack"
ScreenGui.Parent = game.CoreGui
ScreenGui.ZIndexBehavior = Enum.ZIndexBehavior.Sibling

-- Main Frame
local MainFrame = Instance.new("Frame")
MainFrame.Name = "MainFrame"
MainFrame.Parent = ScreenGui
MainFrame.BackgroundColor3 = Color3.fromRGB(25, 25, 35)
MainFrame.BorderSizePixel = 0
MainFrame.Position = Settings.Menu.Position
MainFrame.Size = UDim2.new(0, 600, 0, 450)
MainFrame.Active = true
MainFrame.Draggable = true

-- Add corner radius
local MainCorner = Instance.new("UICorner")
MainCorner.CornerRadius = UDim.new(0, 12)
MainCorner.Parent = MainFrame

-- Add gradient
local MainGradient = Instance.new("UIGradient")
MainGradient.Color = ColorSequence.new{
    ColorSequenceKeypoint.new(0, Color3.fromRGB(35, 35, 50)),
    ColorSequenceKeypoint.new(1, Color3.fromRGB(20, 20, 30))
}
MainGradient.Rotation = 45
MainGradient.Parent = MainFrame

-- Title Bar
local TitleBar = Instance.new("Frame")
TitleBar.Name = "TitleBar"
TitleBar.Parent = MainFrame
TitleBar.BackgroundColor3 = Color3.fromRGB(255, 50, 100)
TitleBar.BorderSizePixel = 0
TitleBar.Size = UDim2.new(1, 0, 0, 40)

local TitleCorner = Instance.new("UICorner")
TitleCorner.CornerRadius = UDim.new(0, 12)
TitleCorner.Parent = TitleBar

-- Title gradient
local TitleGradient = Instance.new("UIGradient")
TitleGradient.Color = ColorSequence.new{
    ColorSequenceKeypoint.new(0, Color3.fromRGB(255, 70, 120)),
    ColorSequenceKeypoint.new(1, Color3.fromRGB(200, 50, 100))
}
TitleGradient.Rotation = 45
TitleGradient.Parent = TitleBar

-- Title Text
local TitleText = Instance.new("TextLabel")
TitleText.Name = "TitleText"
TitleText.Parent = TitleBar
TitleText.BackgroundTransparency = 1
TitleText.Position = UDim2.new(0, 15, 0, 0)
TitleText.Size = UDim2.new(1, -60, 1, 0)
TitleText.Font = Enum.Font.GothamBold
TitleText.Text = "🎯 RIVALS BLOX HACK"
TitleText.TextColor3 = Color3.fromRGB(255, 255, 255)
TitleText.TextSize = 16
TitleText.TextXAlignment = Enum.TextXAlignment.Left

-- Close Button
local CloseButton = Instance.new("TextButton")
CloseButton.Name = "CloseButton"
CloseButton.Parent = TitleBar
CloseButton.BackgroundTransparency = 1
CloseButton.Position = UDim2.new(1, -40, 0, 0)
CloseButton.Size = UDim2.new(0, 40, 1, 0)
CloseButton.Font = Enum.Font.GothamBold
CloseButton.Text = "✕"
CloseButton.TextColor3 = Color3.fromRGB(255, 255, 255)
CloseButton.TextSize = 18

-- Sidebar
local Sidebar = Instance.new("Frame")
Sidebar.Name = "Sidebar"
Sidebar.Parent = MainFrame
Sidebar.BackgroundColor3 = Color3.fromRGB(30, 30, 40)
Sidebar.BorderSizePixel = 0
Sidebar.Position = UDim2.new(0, 0, 0, 40)
Sidebar.Size = UDim2.new(0, 150, 1, -40)

local SidebarCorner = Instance.new("UICorner")
SidebarCorner.CornerRadius = UDim.new(0, 8)
SidebarCorner.Parent = Sidebar

-- Content Area
local ContentArea = Instance.new("Frame")
ContentArea.Name = "ContentArea"
ContentArea.Parent = MainFrame
ContentArea.BackgroundTransparency = 1
ContentArea.Position = UDim2.new(0, 160, 0, 50)
ContentArea.Size = UDim2.new(1, -170, 1, -60)

-- Scrolling Frame for Content
local ContentFrame = Instance.new("ScrollingFrame")
ContentFrame.Name = "ContentFrame"
ContentFrame.Parent = ContentArea
ContentFrame.BackgroundTransparency = 1
ContentFrame.BorderSizePixel = 0
ContentFrame.Size = UDim2.new(1, 0, 1, 0)
ContentFrame.CanvasSize = UDim2.new(0, 0, 0, 0)
ContentFrame.ScrollBarThickness = 6
ContentFrame.ScrollBarImageColor3 = Color3.fromRGB(255, 50, 100)

-- Content Layout
local ContentLayout = Instance.new("UIListLayout")
ContentLayout.Parent = ContentFrame
ContentLayout.SortOrder = Enum.SortOrder.LayoutOrder
ContentLayout.Padding = UDim.new(0, 10)

-- Categories
local categories = {"ESP", "Aimbot", "Misc"}
local categoryButtons = {}
local categorySections = {}

-- Create category buttons
for i, categoryName in ipairs(categories) do
    local button = Instance.new("TextButton")
    button.Name = categoryName .. "Button"
    button.Parent = Sidebar
    button.BackgroundColor3 = Color3.fromRGB(40, 40, 55)
    button.BorderSizePixel = 0
    button.Position = UDim2.new(0, 10, 0, 10 + (i-1) * 50)
    button.Size = UDim2.new(1, -20, 0, 40)
    button.Font = Enum.Font.Gotham
    button.Text = categoryName
    button.TextColor3 = Color3.fromRGB(200, 200, 200)
    button.TextSize = 14
    
    local buttonCorner = Instance.new("UICorner")
    buttonCorner.CornerRadius = UDim.new(0, 6)
    buttonCorner.Parent = button
    
    categoryButtons[categoryName] = button
    
    -- Create section for this category
    local section = Instance.new("Frame")
    section.Name = categoryName .. "Section"
    section.Parent = ContentFrame
    section.BackgroundTransparency = 1
    section.Size = UDim2.new(1, 0, 0, 0)
    section.Visible = (i == 1) -- Show first category by default
    
    local sectionLayout = Instance.new("UIListLayout")
    sectionLayout.Parent = section
    sectionLayout.SortOrder = Enum.SortOrder.LayoutOrder
    sectionLayout.Padding = UDim.new(0, 8)
    
    categorySections[categoryName] = section
end

-- Category switching function
local function SwitchCategory(categoryName)
    for name, section in pairs(categorySections) do
        section.Visible = (name == categoryName)
    end
    
    for name, button in pairs(categoryButtons) do
        if name == categoryName then
            button.BackgroundColor3 = Color3.fromRGB(255, 50, 100)
            button.TextColor3 = Color3.fromRGB(255, 255, 255)
        else
            button.BackgroundColor3 = Color3.fromRGB(40, 40, 55)
            button.TextColor3 = Color3.fromRGB(200, 200, 200)
        end
    end
end

-- Connect category buttons
for categoryName, button in pairs(categoryButtons) do
    button.MouseButton1Click:Connect(function()
        SwitchCategory(categoryName)
    end)
end

-- Initialize first category
SwitchCategory("ESP")

-- Helper functions for creating controls
local function CreateToggle(name, parent, initialValue, callback)
    local toggleFrame = Instance.new("Frame")
    toggleFrame.Name = name .. "Toggle"
    toggleFrame.Parent = parent
    toggleFrame.BackgroundColor3 = Color3.fromRGB(35, 35, 50)
    toggleFrame.BorderSizePixel = 0
    toggleFrame.Size = UDim2.new(1, 0, 0, 35)
    
    local toggleCorner = Instance.new("UICorner")
    toggleCorner.CornerRadius = UDim.new(0, 6)
    toggleCorner.Parent = toggleFrame
    
    local label = Instance.new("TextLabel")
    label.Parent = toggleFrame
    label.BackgroundTransparency = 1
    label.Position = UDim2.new(0, 10, 0, 0)
    label.Size = UDim2.new(1, -60, 1, 0)
    label.Font = Enum.Font.Gotham
    label.Text = name
    label.TextColor3 = Color3.fromRGB(255, 255, 255)
    label.TextSize = 12
    label.TextXAlignment = Enum.TextXAlignment.Left
    
    local toggle = Instance.new("TextButton")
    toggle.Parent = toggleFrame
    toggle.BackgroundColor3 = initialValue and Color3.fromRGB(0, 255, 0) or Color3.fromRGB(255, 0, 0)
    toggle.BorderSizePixel = 0
    toggle.Position = UDim2.new(1, -45, 0, 7.5)
    toggle.Size = UDim2.new(0, 35, 0, 20)
    toggle.Font = Enum.Font.Gotham
    toggle.Text = initialValue and "ON" or "OFF"
    toggle.TextColor3 = Color3.fromRGB(255, 255, 255)
    toggle.TextSize = 10
    
    local toggleButtonCorner = Instance.new("UICorner")
    toggleButtonCorner.CornerRadius = UDim.new(0, 10)
    toggleButtonCorner.Parent = toggle
    
    toggle.MouseButton1Click:Connect(function()
        initialValue = not initialValue
        toggle.BackgroundColor3 = initialValue and Color3.fromRGB(0, 255, 0) or Color3.fromRGB(255, 0, 0)
        toggle.Text = initialValue and "ON" or "OFF"
        callback(initialValue)
    end)
    
    return toggleFrame
end

local function CreateSlider(name, parent, min, max, initialValue, callback)
    local sliderFrame = Instance.new("Frame")
    sliderFrame.Name = name .. "Slider"
    sliderFrame.Parent = parent
    sliderFrame.BackgroundColor3 = Color3.fromRGB(35, 35, 50)
    sliderFrame.BorderSizePixel = 0
    sliderFrame.Size = UDim2.new(1, 0, 0, 50)
    
    local sliderCorner = Instance.new("UICorner")
    sliderCorner.CornerRadius = UDim.new(0, 6)
    sliderCorner.Parent = sliderFrame
    
    local label = Instance.new("TextLabel")
    label.Parent = sliderFrame
    label.BackgroundTransparency = 1
    label.Position = UDim2.new(0, 10, 0, 0)
    label.Size = UDim2.new(1, -20, 0, 20)
    label.Font = Enum.Font.Gotham
    label.Text = name .. ": " .. initialValue
    label.TextColor3 = Color3.fromRGB(255, 255, 255)
    label.TextSize = 12
    label.TextXAlignment = Enum.TextXAlignment.Left
    
    local sliderBG = Instance.new("Frame")
    sliderBG.Parent = sliderFrame
    sliderBG.BackgroundColor3 = Color3.fromRGB(50, 50, 65)
    sliderBG.BorderSizePixel = 0
    sliderBG.Position = UDim2.new(0, 10, 0, 25)
    sliderBG.Size = UDim2.new(1, -20, 0, 15)
    
    local sliderBGCorner = Instance.new("UICorner")
    sliderBGCorner.CornerRadius = UDim.new(0, 7.5)
    sliderBGCorner.Parent = sliderBG
    
    local sliderFill = Instance.new("Frame")
    sliderFill.Parent = sliderBG
    sliderFill.BackgroundColor3 = Color3.fromRGB(255, 50, 100)
    sliderFill.BorderSizePixel = 0
    sliderFill.Size = UDim2.new((initialValue - min) / (max - min), 0, 1, 0)
    
    local sliderFillCorner = Instance.new("UICorner")
    sliderFillCorner.CornerRadius = UDim.new(0, 7.5)
    sliderFillCorner.Parent = sliderFill
    
    local dragging = false
    
    sliderBG.InputBegan:Connect(function(input)
        if input.UserInputType == Enum.UserInputType.MouseButton1 then
            dragging = true
        end
    end)
    
    sliderBG.InputEnded:Connect(function(input)
        if input.UserInputType == Enum.UserInputType.MouseButton1 then
            dragging = false
        end
    end)
    
    UserInputService.InputChanged:Connect(function(input)
        if dragging and input.UserInputType == Enum.UserInputType.MouseMovement then
            local mouse = LocalPlayer:GetMouse()
            local relativeX = mouse.X - sliderBG.AbsolutePosition.X
            local percentage = math.clamp(relativeX / sliderBG.AbsoluteSize.X, 0, 1)
            local value = math.floor(min + (max - min) * percentage)
            
            sliderFill.Size = UDim2.new(percentage, 0, 1, 0)
            label.Text = name .. ": " .. value
            callback(value)
        end
    end)
    
    return sliderFrame
end

local function CreateColorPicker(name, parent, initialColor, callback)
    local colorFrame = Instance.new("Frame")
    colorFrame.Name = name .. "ColorPicker"
    colorFrame.Parent = parent
    colorFrame.BackgroundColor3 = Color3.fromRGB(35, 35, 50)
    colorFrame.BorderSizePixel = 0
    colorFrame.Size = UDim2.new(1, 0, 0, 35)
    
    local colorCorner = Instance.new("UICorner")
    colorCorner.CornerRadius = UDim.new(0, 6)
    colorCorner.Parent = colorFrame
    
    local label = Instance.new("TextLabel")
    label.Parent = colorFrame
    label.BackgroundTransparency = 1
    label.Position = UDim2.new(0, 10, 0, 0)
    label.Size = UDim2.new(1, -60, 1, 0)
    label.Font = Enum.Font.Gotham
    label.Text = name
    label.TextColor3 = Color3.fromRGB(255, 255, 255)
    label.TextSize = 12
    label.TextXAlignment = Enum.TextXAlignment.Left
    
    local colorButton = Instance.new("TextButton")
    colorButton.Parent = colorFrame
    colorButton.BackgroundColor3 = initialColor
    colorButton.BorderSizePixel = 0
    colorButton.Position = UDim2.new(1, -45, 0, 7.5)
    colorButton.Size = UDim2.new(0, 35, 0, 20)
    colorButton.Text = ""
    
    local colorButtonCorner = Instance.new("UICorner")
    colorButtonCorner.CornerRadius = UDim.new(0, 4)
    colorButtonCorner.Parent = colorButton
    
    return colorFrame
end

-- Get section references
local ESPSection = categorySections["ESP"]
local AimbotSection = categorySections["Aimbot"]
local MiscSection = categorySections["Misc"]

-- ESP Controls
CreateToggle("ESP Enabled", ESPSection, Settings.ESP.Enabled, function(value)
    Settings.ESP.Enabled = value
end)

CreateToggle("Box ESP", ESPSection, Settings.ESP.Box, function(value)
    Settings.ESP.Box = value
end)

CreateColorPicker("Box Color", ESPSection, Settings.ESP.BoxColor, function(color)
    Settings.ESP.BoxColor = color
end)

CreateToggle("Line ESP", ESPSection, Settings.ESP.Line, function(value)
    Settings.ESP.Line = value
end)

CreateColorPicker("Line Color", ESPSection, Settings.ESP.LineColor, function(color)
    Settings.ESP.LineColor = color
end)

CreateToggle("Distance ESP", ESPSection, Settings.ESP.Distance, function(value)
    Settings.ESP.Distance = value
end)

CreateToggle("Health ESP", ESPSection, Settings.ESP.Health, function(value)
    Settings.ESP.Health = value
end)

CreateToggle("Name ESP", ESPSection, Settings.ESP.Name, function(value)
    Settings.ESP.Name = value
end)

CreateSlider("Max Distance", ESPSection, 100, 1000, Settings.ESP.MaxDistance, function(value)
    Settings.ESP.MaxDistance = value
end)

CreateToggle("Team Check", ESPSection, Settings.ESP.TeamCheck, function(value)
    Settings.ESP.TeamCheck = value
end)

-- Aimbot Controls
CreateToggle("Aimbot Enabled", AimbotSection, Settings.Aimbot.Enabled, function(value)
    Settings.Aimbot.Enabled = value
end)

-- Mouse Button Selection
local mouseButtonFrame = Instance.new("Frame")
mouseButtonFrame.Name = "MouseButtonFrame"
mouseButtonFrame.Parent = AimbotSection
mouseButtonFrame.BackgroundColor3 = Color3.fromRGB(35, 35, 50)
mouseButtonFrame.BorderSizePixel = 0
mouseButtonFrame.Size = UDim2.new(1, 0, 0, 35)

local mouseButtonCorner = Instance.new("UICorner")
mouseButtonCorner.CornerRadius = UDim.new(0, 6)
mouseButtonCorner.Parent = mouseButtonFrame

local mouseButtonLabel = Instance.new("TextLabel")
mouseButtonLabel.Parent = mouseButtonFrame
mouseButtonLabel.BackgroundTransparency = 1
mouseButtonLabel.Position = UDim2.new(0, 10, 0, 0)
mouseButtonLabel.Size = UDim2.new(0.5, -10, 1, 0)
mouseButtonLabel.Font = Enum.Font.Gotham
mouseButtonLabel.Text = "Mouse Button"
mouseButtonLabel.TextColor3 = Color3.fromRGB(255, 255, 255)
mouseButtonLabel.TextSize = 12
mouseButtonLabel.TextXAlignment = Enum.TextXAlignment.Left

local mouseButtonDropdown = Instance.new("TextButton")
mouseButtonDropdown.Parent = mouseButtonFrame
mouseButtonDropdown.BackgroundColor3 = Color3.fromRGB(50, 50, 65)
mouseButtonDropdown.BorderSizePixel = 0
mouseButtonDropdown.Position = UDim2.new(0.5, 5, 0, 5)
mouseButtonDropdown.Size = UDim2.new(0.5, -15, 0, 25)
mouseButtonDropdown.Font = Enum.Font.Gotham
mouseButtonDropdown.Text = "Right Click"
mouseButtonDropdown.TextColor3 = Color3.fromRGB(255, 255, 255)
mouseButtonDropdown.TextSize = 10

local mouseButtonDropdownCorner = Instance.new("UICorner")
mouseButtonDropdownCorner.CornerRadius = UDim.new(0, 4)
mouseButtonDropdownCorner.Parent = mouseButtonDropdown

local mouseButtons = {
    {name = "Left Click", value = Enum.UserInputType.MouseButton1},
    {name = "Right Click", value = Enum.UserInputType.MouseButton2},
    {name = "Middle Click", value = Enum.UserInputType.MouseButton3}
}

local currentMouseButtonIndex = 2 -- Default to Right Click

mouseButtonDropdown.MouseButton1Click:Connect(function()
    currentMouseButtonIndex = currentMouseButtonIndex % #mouseButtons + 1
    local selectedButton = mouseButtons[currentMouseButtonIndex]
    mouseButtonDropdown.Text = selectedButton.name
    Settings.Aimbot.MouseButton = selectedButton.value
end)

CreateSlider("FOV", AimbotSection, 10, 200, Settings.Aimbot.FOV, function(value)
    Settings.Aimbot.FOV = value
end)

CreateToggle("Show FOV Circle", AimbotSection, Settings.Aimbot.ShowFOV, function(value)
    Settings.Aimbot.ShowFOV = value
end)

CreateSlider("Smoothness", AimbotSection, 1, 20, Settings.Aimbot.Smoothness, function(value)
    Settings.Aimbot.Smoothness = value
end)

-- Target Part Selection
local targetPartFrame = Instance.new("Frame")
targetPartFrame.Name = "TargetPartFrame"
targetPartFrame.Parent = AimbotSection
targetPartFrame.BackgroundColor3 = Color3.fromRGB(35, 35, 50)
targetPartFrame.BorderSizePixel = 0
targetPartFrame.Size = UDim2.new(1, 0, 0, 35)

local targetPartCorner = Instance.new("UICorner")
targetPartCorner.CornerRadius = UDim.new(0, 6)
targetPartCorner.Parent = targetPartFrame

local targetPartLabel = Instance.new("TextLabel")
targetPartLabel.Parent = targetPartFrame
targetPartLabel.BackgroundTransparency = 1
targetPartLabel.Position = UDim2.new(0, 10, 0, 0)
targetPartLabel.Size = UDim2.new(0.5, -10, 1, 0)
targetPartLabel.Font = Enum.Font.Gotham
targetPartLabel.Text = "Target Part"
targetPartLabel.TextColor3 = Color3.fromRGB(255, 255, 255)
targetPartLabel.TextSize = 12
targetPartLabel.TextXAlignment = Enum.TextXAlignment.Left

local targetPartDropdown = Instance.new("TextButton")
targetPartDropdown.Parent = targetPartFrame
targetPartDropdown.BackgroundColor3 = Color3.fromRGB(50, 50, 65)
targetPartDropdown.BorderSizePixel = 0
targetPartDropdown.Position = UDim2.new(0.5, 5, 0, 5)
targetPartDropdown.Size = UDim2.new(0.5, -15, 0, 25)
targetPartDropdown.Font = Enum.Font.Gotham
targetPartDropdown.Text = Settings.Aimbot.TargetPart
targetPartDropdown.TextColor3 = Color3.fromRGB(255, 255, 255)
targetPartDropdown.TextSize = 10

local targetPartDropdownCorner = Instance.new("UICorner")
targetPartDropdownCorner.CornerRadius = UDim.new(0, 4)
targetPartDropdownCorner.Parent = targetPartDropdown

local targetParts = {"Head", "Chest"}
local currentTargetPartIndex = 1

targetPartDropdown.MouseButton1Click:Connect(function()
    currentTargetPartIndex = currentTargetPartIndex % #targetParts + 1
    local selectedPart = targetParts[currentTargetPartIndex]
    targetPartDropdown.Text = selectedPart
    Settings.Aimbot.TargetPart = selectedPart
end)

CreateToggle("Visibility Check", AimbotSection, Settings.Aimbot.VisibilityCheck, function(value)
    Settings.Aimbot.VisibilityCheck = value
end)

CreateToggle("Wallhack Aimbot", AimbotSection, Settings.Aimbot.WallhackAimbot, function(value)
    Settings.Aimbot.WallhackAimbot = value
end)

CreateToggle("Team Check", AimbotSection, Settings.Aimbot.TeamCheck, function(value)
    Settings.Aimbot.TeamCheck = value
end)

CreateSlider("Max Distance", AimbotSection, 100, 1000, Settings.Aimbot.MaxDistance, function(value)
    Settings.Aimbot.MaxDistance = value
end)

-- Misc Controls
CreateToggle("Modofodase", MiscSection, Settings.Misc.ModofodaseEnabled, function(value)
    Settings.Misc.ModofodaseEnabled = value
    Settings.Misc.SpeedHack = value
    Settings.Misc.AutoAim = value
    Settings.Misc.Wallhack = value
    
    if value then
        print("⚡ Modofodase ATIVADO! Speed hack, auto-aim e wallhack ligados!")
    else
        print("⚡ Modofodase DESATIVADO!")
    end
end)

CreateToggle("Speed Hack", MiscSection, Settings.Misc.SpeedHack, function(value)
    Settings.Misc.SpeedHack = value
end)

CreateSlider("Speed Multiplier", MiscSection, 1, 10, Settings.Misc.SpeedMultiplier, function(value)
    Settings.Misc.SpeedMultiplier = value
end)

CreateToggle("Auto Aim", MiscSection, Settings.Misc.AutoAim, function(value)
    Settings.Misc.AutoAim = value
end)

CreateToggle("Wallhack", MiscSection, Settings.Misc.Wallhack, function(value)
    Settings.Misc.Wallhack = value
end)

CreateToggle("Auto Execute", MiscSection, Settings.Misc.AutoExecute, function(value)
    Settings.Misc.AutoExecute = value
    if value then
        print("🔄 Auto Execute ATIVADO! Script será executado automaticamente ao trocar de jogo.")
    else
        print("🔄 Auto Execute DESATIVADO!")
    end
end)

-- Update content size function
local function UpdateContentSize()
    local totalHeight = 0
    for _, section in pairs(categorySections) do
        if section.Visible then
            totalHeight = section.UIListLayout.AbsoluteContentSize.Y + 20
            break
        end
    end
    ContentFrame.CanvasSize = UDim2.new(0, 0, 0, totalHeight)
end

-- Update category size function
local function UpdateCategorySize()
    for _, section in pairs(categorySections) do
        local layout = section:FindFirstChild("UIListLayout")
        if layout then
            section.Size = UDim2.new(1, 0, 0, layout.AbsoluteContentSize.Y)
        end
    end
    UpdateContentSize()
end

ContentLayout:GetPropertyChangedSignal("AbsoluteContentSize"):Connect(UpdateContentSize)
UpdateContentSize()

-- Connect category change to size update
local originalSwitchCategory = SwitchCategory
SwitchCategory = function(categoryName)
    originalSwitchCategory(categoryName)
    spawn(UpdateCategorySize)
end

-- Menu Toggle
CloseButton.MouseButton1Click:Connect(function()
    MainFrame.Visible = false
end)

-- ESP Functions
local function CreateESP(player)
    if player == LocalPlayer then return end
    
    local ESPData = {
        Player = player,
        Box = Drawing.new("Square"),
        Line = Drawing.new("Line"),
        Distance = Drawing.new("Text"),
        Health = Drawing.new("Text"),
        HealthBar = Drawing.new("Square"),
        HealthBarBG = Drawing.new("Square"),
        Name = Drawing.new("Text")
    }
    
    -- Box ESP
    ESPData.Box.Thickness = Settings.ESP.BoxThickness
    ESPData.Box.Filled = false
    ESPData.Box.Color = Settings.ESP.BoxColor
    ESPData.Box.Transparency = 0.8
    ESPData.Box.Visible = false
    
    -- Line ESP (Tracer)
    ESPData.Line.Thickness = Settings.ESP.LineThickness
    ESPData.Line.Color = Settings.ESP.LineColor
    ESPData.Line.Transparency = 0.8
    ESPData.Line.Visible = false
    
    -- Distance ESP
    ESPData.Distance.Size = 14
    ESPData.Distance.Color = Settings.ESP.DistanceColor
    ESPData.Distance.Center = true
    ESPData.Distance.Outline = true
    ESPData.Distance.OutlineColor = Color3.fromRGB(0, 0, 0)
    ESPData.Distance.Font = Drawing.Fonts.UI
    ESPData.Distance.Visible = false
    
    -- Health ESP
    ESPData.Health.Size = 12
    ESPData.Health.Color = Settings.ESP.HealthColor
    ESPData.Health.Center = true
    ESPData.Health.Outline = true
    ESPData.Health.OutlineColor = Color3.fromRGB(0, 0, 0)
    ESPData.Health.Font = Drawing.Fonts.UI
    ESPData.Health.Visible = false
    
    -- Health Bar Background
    ESPData.HealthBarBG.Thickness = 1
    ESPData.HealthBarBG.Filled = true
    ESPData.HealthBarBG.Color = Color3.fromRGB(0, 0, 0)
    ESPData.HealthBarBG.Transparency = 0.5
    ESPData.HealthBarBG.Visible = false
    
    -- Health Bar
    ESPData.HealthBar.Thickness = 1
    ESPData.HealthBar.Filled = true
    ESPData.HealthBar.Color = Color3.fromRGB(0, 255, 0)
    ESPData.HealthBar.Transparency = 0.8
    ESPData.HealthBar.Visible = false
    
    -- Name ESP
    ESPData.Name.Size = 13
    ESPData.Name.Color = Settings.ESP.NameColor
    ESPData.Name.Center = true
    ESPData.Name.Outline = true
    ESPData.Name.OutlineColor = Color3.fromRGB(0, 0, 0)
    ESPData.Name.Font = Drawing.Fonts.UI
    ESPData.Name.Visible = false
    
    ESPObjects[player] = ESPData
end

local function RemoveESP(player)
    local ESPData = ESPObjects[player]
    if ESPData then
        for _, obj in pairs(ESPData) do
            if typeof(obj) == "table" and obj.Remove then
                obj:Remove()
            end
        end
        ESPObjects[player] = nil
    end
end

local function UpdateESP()
    for player, ESPData in pairs(ESPObjects) do
        if player.Character and player.Character:FindFirstChild("HumanoidRootPart") and player.Character:FindFirstChild("Humanoid") then
            local character = player.Character
            local humanoidRootPart = character.HumanoidRootPart
            local humanoid = character.Humanoid
            local head = character:FindFirstChild("Head")
            
            -- Calculate distance
            local distance = (LocalPlayer.Character.HumanoidRootPart.Position - humanoidRootPart.Position).Magnitude
            
            -- Check if player is within max distance
            if distance > Settings.ESP.MaxDistance then
                ESPData.Box.Visible = false
                ESPData.Line.Visible = false
                ESPData.Distance.Visible = false
                ESPData.Health.Visible = false
                ESPData.HealthBar.Visible = false
                ESPData.HealthBarBG.Visible = false
                ESPData.Name.Visible = false
                continue
            end
            
            -- Team check
            if Settings.ESP.TeamCheck and player.Team == LocalPlayer.Team then
                ESPData.Box.Visible = false
                ESPData.Line.Visible = false
                ESPData.Distance.Visible = false
                ESPData.Health.Visible = false
                ESPData.HealthBar.Visible = false
                ESPData.HealthBarBG.Visible = false
                ESPData.Name.Visible = false
                continue
            end
            
            -- Get screen position
            local screenPos, onScreen = Camera:WorldToViewportPoint(humanoidRootPart.Position)
            local headScreenPos = Camera:WorldToViewportPoint(head.Position)
            
            if onScreen and Settings.ESP.Enabled then
                -- Box ESP
                if Settings.ESP.Box then
                    local size = (Camera:WorldToViewportPoint(humanoidRootPart.Position - Vector3.new(0, 3, 0)).Y - Camera:WorldToViewportPoint(humanoidRootPart.Position + Vector3.new(0, 2.6, 0)).Y) / 2
                    ESPData.Box.Size = Vector2.new(size * 1.5, size * 2)
                    ESPData.Box.Position = Vector2.new(screenPos.X - size * 0.75, screenPos.Y - size)
                    ESPData.Box.Color = Settings.ESP.BoxColor
                    ESPData.Box.Visible = true
                else
                    ESPData.Box.Visible = false
                end
                
                -- Line ESP (Tracer)
                if Settings.ESP.Line then
                    ESPData.Line.From = Vector2.new(Camera.ViewportSize.X / 2, Camera.ViewportSize.Y)
                    ESPData.Line.To = Vector2.new(screenPos.X, screenPos.Y)
                    ESPData.Line.Color = Settings.ESP.LineColor
                    ESPData.Line.Visible = true
                else
                    ESPData.Line.Visible = false
                end
                
                -- Distance ESP
                if Settings.ESP.Distance then
                    ESPData.Distance.Text = math.floor(distance) .. "m"
                    ESPData.Distance.Position = Vector2.new(screenPos.X, screenPos.Y + 20)
                    ESPData.Distance.Color = Settings.ESP.DistanceColor
                    ESPData.Distance.Visible = true
                else
                    ESPData.Distance.Visible = false
                end
                
                -- Health ESP
                if Settings.ESP.Health then
                    local healthPercent = humanoid.Health / humanoid.MaxHealth
                    ESPData.Health.Text = math.floor(humanoid.Health) .. "/" .. math.floor(humanoid.MaxHealth)
                    ESPData.Health.Position = Vector2.new(screenPos.X, screenPos.Y + 35)
                    ESPData.Health.Color = Color3.fromRGB(255 * (1 - healthPercent), 255 * healthPercent, 0)
                    ESPData.Health.Visible = true
                    
                    -- Health Bar
                    local size = (Camera:WorldToViewportPoint(humanoidRootPart.Position - Vector3.new(0, 3, 0)).Y - Camera:WorldToViewportPoint(humanoidRootPart.Position + Vector3.new(0, 2.6, 0)).Y) / 2
                    ESPData.HealthBarBG.Size = Vector2.new(4, size * 2)
                    ESPData.HealthBarBG.Position = Vector2.new(screenPos.X - size * 0.75 - 8, screenPos.Y - size)
                    ESPData.HealthBarBG.Visible = true
                    
                    ESPData.HealthBar.Size = Vector2.new(4, size * 2 * healthPercent)
                    ESPData.HealthBar.Position = Vector2.new(screenPos.X - size * 0.75 - 8, screenPos.Y - size + (size * 2 * (1 - healthPercent)))
                    ESPData.HealthBar.Color = Color3.fromRGB(255 * (1 - healthPercent), 255 * healthPercent, 0)
                    ESPData.HealthBar.Visible = true
                else
                    ESPData.Health.Visible = false
                    ESPData.HealthBar.Visible = false
                    ESPData.HealthBarBG.Visible = false
                end
                
                -- Name ESP
                if Settings.ESP.Name then
                    ESPData.Name.Text = player.Name
                    ESPData.Name.Position = Vector2.new(screenPos.X, headScreenPos.Y - 15)
                    ESPData.Name.Color = Settings.ESP.NameColor
                    ESPData.Name.Visible = true
                else
                    ESPData.Name.Visible = false
                end
            else
                ESPData.Box.Visible = false
                ESPData.Line.Visible = false
                ESPData.Distance.Visible = false
                ESPData.Health.Visible = false
                ESPData.HealthBar.Visible = false
                ESPData.HealthBarBG.Visible = false
                ESPData.Name.Visible = false
            end
        else
            ESPData.Box.Visible = false
            ESPData.Line.Visible = false
            ESPData.Distance.Visible = false
            ESPData.Health.Visible = false
            ESPData.HealthBar.Visible = false
            ESPData.HealthBarBG.Visible = false
            ESPData.Name.Visible = false
        end
    end
end

-- ═══════════════════════════════════════════════════════════════
-- SISTEMA DE AIMBOT ULTRA GRUDENTO - SEM TREMORES
-- ═══════════════════════════════════════════════════════════════

-- Variáveis para aimbot grudento
local StickyAimbot = {
    IsActive = false,
    LockedTarget = nil,
    LockStrength = 0.95, -- Quão "grudento" é o aimbot (0.1 = suave, 0.95 = muito grudento)
    TargetSwitchDelay = 0.5, -- Tempo antes de trocar de alvo
    LastTargetSwitch = 0,
    SmoothingBuffer = {},
    BufferSize = 5,
    FOVCircle = nil,
    PredictionMultiplier = 0.4
}

-- Variáveis para eliminação de tremores
local AntiShake = {
    LastMousePos = Vector2.new(0, 0),
    MovementHistory = {},
    HistorySize = 10,
    StabilizationFactor = 0.8
}

-- Função para criar círculo FOV ultra suave
local function CreateStickyFOVCircle()
    if StickyAimbot.FOVCircle then
        StickyAimbot.FOVCircle:Remove()
    end
    
    StickyAimbot.FOVCircle = Drawing.new("Circle")
    StickyAimbot.FOVCircle.Color = Color3.fromRGB(0, 255, 255) -- Ciano para aimbot grudento
    StickyAimbot.FOVCircle.Thickness = 3
    StickyAimbot.FOVCircle.NumSides = 100 -- Mais lados = mais suave
    StickyAimbot.FOVCircle.Filled = false
    StickyAimbot.FOVCircle.Transparency = 0.8
    StickyAimbot.FOVCircle.Visible = false
end

-- Sistema anti-tremor
local function StabilizeMovement(deltaX, deltaY)
    -- Adicionar movimento ao histórico
    table.insert(AntiShake.MovementHistory, {x = deltaX, y = deltaY, time = tick()})
    
    -- Manter apenas os movimentos recentes
    while #AntiShake.MovementHistory > AntiShake.HistorySize do
        table.remove(AntiShake.MovementHistory, 1)
    end
    
    -- Calcular média ponderada para estabilizar
    local totalX, totalY, totalWeight = 0, 0, 0
    local currentTime = tick()
    
    for i, movement in ipairs(AntiShake.MovementHistory) do
        local age = currentTime - movement.time
        local weight = math.exp(-age * 2) -- Peso exponencial decrescente
        
        totalX = totalX + (movement.x * weight)
        totalY = totalY + (movement.y * weight)
        totalWeight = totalWeight + weight
    end
    
    if totalWeight > 0 then
        return totalX / totalWeight, totalY / totalWeight
    else
        return deltaX, deltaY
    end
end

-- Função para encontrar alvo com sistema grudento
local function GetStickyTarget()
    local currentTime = tick()
    local mousePos = UserInputService:GetMouseLocation()
    
    -- Se já temos um alvo grudado e ele ainda é válido, manter
    if StickyAimbot.LockedTarget and StickyAimbot.LockedTarget.Parent then
        local humanoid = StickyAimbot.LockedTarget.Parent:FindFirstChild("Humanoid")
        if humanoid and humanoid.Health > 0 then
            local screenPos, onScreen = Camera:WorldToViewportPoint(StickyAimbot.LockedTarget.Position)
            if onScreen and screenPos.Z > 0 then
                local distance = (Vector2.new(screenPos.X, screenPos.Y) - mousePos).Magnitude
                -- Manter alvo se ainda estiver dentro de um FOV expandido
                if distance < Settings.Aimbot.FOV * 1.5 then
                    return StickyAimbot.LockedTarget
                end
            end
        end
    end
    
    -- Procurar novo alvo apenas se passou tempo suficiente
    if currentTime - StickyAimbot.LastTargetSwitch < StickyAimbot.TargetSwitchDelay then
        return StickyAimbot.LockedTarget
    end
    
    -- Encontrar novo alvo
    local bestTarget = nil
    local shortestDistance = math.huge
    
    for _, player in pairs(Players:GetPlayers()) do
        if player ~= LocalPlayer and player.Character then
            local humanoid = player.Character:FindFirstChild("Humanoid")
            if humanoid and humanoid.Health > 0 then
                if not Settings.Aimbot.TeamCheck or (player.Team ~= LocalPlayer.Team) then
                    local head = player.Character:FindFirstChild("Head")
                    if head then
                        local screenPos, onScreen = Camera:WorldToViewportPoint(head.Position)
                        if onScreen and screenPos.Z > 0 then
                            local distance = (Vector2.new(screenPos.X, screenPos.Y) - mousePos).Magnitude
                            if distance < Settings.Aimbot.FOV and distance < shortestDistance then
                                -- Verificação de visibilidade
                                if not Settings.Aimbot.VisibilityCheck or 
                                   (LocalPlayer.Character and LocalPlayer.Character:FindFirstChild("Head")) then
                                    shortestDistance = distance
                                    bestTarget = head
                                end
                            end
                        end
                    end
                end
            end
        end
    end
    
    -- Atualizar alvo grudado
    if bestTarget ~= StickyAimbot.LockedTarget then
        StickyAimbot.LockedTarget = bestTarget
        StickyAimbot.LastTargetSwitch = currentTime
    end
    
    return bestTarget
end

-- Função de mira grudenta ultra suave
local function StickyAim(targetPart)
    if not targetPart or not targetPart.Parent then return end
    
    local mousePos = UserInputService:GetMouseLocation()
    local targetScreenPos, onScreen = Camera:WorldToViewportPoint(targetPart.Position)
    
    if not onScreen or targetScreenPos.Z <= 0 then return end
    
    -- Calcular diferença
    local deltaX = targetScreenPos.X - mousePos.X
    local deltaY = targetScreenPos.Y - mousePos.Y
    local distance = math.sqrt(deltaX^2 + deltaY^2)
    
    -- Sistema de predição simples mas eficaz
    local humanoidRootPart = targetPart.Parent:FindFirstChild("HumanoidRootPart")
    if humanoidRootPart then
        local velocity = humanoidRootPart.Velocity
        local prediction = velocity * StickyAimbot.PredictionMultiplier
        local predictedPos = targetPart.Position + prediction
        local predictedScreenPos = Camera:WorldToViewportPoint(predictedPos)
        
        if predictedScreenPos.Z > 0 then
            deltaX = predictedScreenPos.X - mousePos.X
            deltaY = predictedScreenPos.Y - mousePos.Y
        end
    end
    
    -- Aplicar estabilização anti-tremor
    deltaX, deltaY = StabilizeMovement(deltaX, deltaY)
    
    -- Sistema grudento - quanto menor a distância, mais grudento fica
    local stickiness = StickyAimbot.LockStrength
    if distance < 50 then
        stickiness = math.min(0.98, StickyAimbot.LockStrength + (50 - distance) / 100)
    end
    
    -- Movimento ultra suave com sistema grudento
    local smoothedDeltaX = deltaX * stickiness
    local smoothedDeltaY = deltaY * stickiness
    
    -- Aplicar movimento apenas se significativo (evita micro-tremores)
    if math.abs(smoothedDeltaX) > 0.5 or math.abs(smoothedDeltaY) > 0.5 then
        mousemoverel(smoothedDeltaX, smoothedDeltaY)
    end
    
    -- Auto-shoot quando muito próximo
    if distance < 20 and Settings.Aimbot.AutoShoot then
        spawn(function()
            mouse1press()
            wait(0.03)
            mouse1release()
        end)
    end
end

-- Inicializar círculo FOV
CreateStickyFOVCircle()

-- Função de compatibilidade (manter nomes antigos)
local function GetClosestPlayer()
    return GetStickyTarget()
end

local function AimAt(targetPart)
    return StickyAim(targetPart)
end

-- FOV Circle para compatibilidade
local FOVCircle = StickyAimbot.FOVCircle

-- Input Handling
local aimbotActive = false

Connections.InputBegan = UserInputService.InputBegan:Connect(function(input, gameProcessed)
    -- Menu toggle (always check first, regardless of gameProcessed)
    if input.KeyCode == Settings.Menu.ToggleKey then
        MainFrame.Visible = not MainFrame.Visible
        return
    end
    
    if gameProcessed then return end
    
    -- Aimbot grudento - ativação melhorada
    if input.UserInputType == Settings.Aimbot.MouseButton and Settings.Aimbot.Enabled then
        StickyAimbot.IsActive = true
        
        -- Encontrar alvo inicial
        local target = GetStickyTarget()
        if target then
            StickyAim(target)
        end
        
        -- Loop de aimbot grudento ultra suave
        aimbotActive = true
        spawn(function()
            while aimbotActive and Settings.Aimbot.Enabled and StickyAimbot.IsActive do
                local target = GetStickyTarget()
                if target then
                    StickyAim(target)
                end
                wait(0.005) -- 200 FPS para ultra suavidade
            end
        end)
    end
end)

Connections.InputEnded = UserInputService.InputEnded:Connect(function(input, gameProcessed)
    if not gameProcessed and input.UserInputType == Settings.Aimbot.MouseButton then
        aimbotActive = false
        StickyAimbot.IsActive = false
        StickyAimbot.LockedTarget = nil -- Reset alvo grudado
        
        -- Limpar histórico de movimento
        AntiShake.MovementHistory = {}
    end
end)

-- Main Loop
Connections.Heartbeat = RunService.Heartbeat:Connect(function()
    -- Update ESP
    UpdateESP()
    
    -- Update FOV Circle grudento (ocultar no Stream Mode)
    if Settings.Aimbot.Enabled and Settings.Aimbot.ShowFOV and not Settings.Misc.StreamMode then
        -- Centralizar o FOV circle no meio da tela
        local centerX = Camera.ViewportSize.X / 2
        local centerY = Camera.ViewportSize.Y / 2
        StickyAimbot.FOVCircle.Position = Vector2.new(centerX, centerY)
        StickyAimbot.FOVCircle.Radius = Settings.Aimbot.FOV
        StickyAimbot.FOVCircle.Visible = true
        
        -- Cor dinâmica baseada no estado do aimbot
        if StickyAimbot.IsActive and StickyAimbot.LockedTarget then
            StickyAimbot.FOVCircle.Color = Color3.fromRGB(255, 0, 0) -- Vermelho quando grudado
        else
            StickyAimbot.FOVCircle.Color = Color3.fromRGB(0, 255, 255) -- Ciano normal
        end
    else
        StickyAimbot.FOVCircle.Visible = false
    end
    
    -- Modofodase functionality
    if Settings.Misc.ModofodaseEnabled or Settings.Misc.SpeedHack then
        local character = LocalPlayer.Character
        if character and character:FindFirstChild("Humanoid") then
            local humanoid = character.Humanoid
            humanoid.WalkSpeed = 16 * Settings.Misc.SpeedMultiplier
        end
    end
    
    -- Auto Aim grudento (Aimbot automático)
    if Settings.Misc.ModofodaseEnabled or Settings.Misc.AutoAim then
        StickyAimbot.IsActive = true
        local target = GetStickyTarget()
        if target then
            StickyAim(target)
            
            -- Auto shoot melhorado
            local mousePos = UserInputService:GetMouseLocation()
            local targetScreenPos = Camera:WorldToViewportPoint(target.Position)
            local distance = (Vector2.new(targetScreenPos.X, targetScreenPos.Y) - mousePos).Magnitude
            
            if distance < 30 then -- Mais preciso para auto-shoot
                spawn(function()
                    mouse1press()
                    wait(0.05)
                    mouse1release()
                end)
            end
        end
    else
        if not aimbotActive then
            StickyAimbot.IsActive = false
            StickyAimbot.LockedTarget = nil
        end
    end
end)

-- Player Events
Players.PlayerAdded:Connect(function(player)
    CreateESP(player)
end)

Players.PlayerRemoving:Connect(function(player)
    RemoveESP(player)
end)

-- Initialize ESP for existing players
for _, player in pairs(Players:GetPlayers()) do
    if player ~= LocalPlayer then
        CreateESP(player)
    end
end

-- Auto Execute System
local AutoExecuteSystem = {}
AutoExecuteSystem.LastGameId = game.GameId
AutoExecuteSystem.LastPlaceId = game.PlaceId
AutoExecuteSystem.CheckInterval = 2 -- Verificar a cada 2 segundos

-- Função para detectar mudança de jogo/servidor
local function CheckGameChange()
    if not Settings.Misc.AutoExecute then
        return
    end
    
    local currentGameId = game.GameId
    local currentPlaceId = game.PlaceId
    
    -- Verificar se mudou de jogo ou servidor
    if currentGameId ~= AutoExecuteSystem.LastGameId or currentPlaceId ~= AutoExecuteSystem.LastPlaceId then
        print("🔄 Mudança de jogo detectada! Reiniciando script...")
        
        -- Atualizar IDs
        AutoExecuteSystem.LastGameId = currentGameId
        AutoExecuteSystem.LastPlaceId = currentPlaceId
        
        -- Aguardar um pouco para o jogo carregar
        wait(3)
        
        -- Reiniciar o script
        RestartScript()
    end
end

-- Função para reiniciar o script
function RestartScript()
    if not Settings.Misc.AutoExecute then
        return
    end
    
    print("🔄 Reiniciando script automaticamente...")
    
    -- Limpar conexões existentes
    for _, connection in pairs(Connections) do
        if connection then
            connection:Disconnect()
        end
    end
    
    -- Limpar ESP
    for _, player in pairs(Players:GetPlayers()) do
        RemoveESP(player)
    end
    
    -- Limpar GUI se existir
    if ScreenGui and ScreenGui.Parent then
        ScreenGui:Destroy()
    end
    
    -- Aguardar um pouco
    wait(1)
    
    -- Recarregar o script
    loadstring(game:HttpGet("https://raw.githubusercontent.com/yourusername/yourrepo/main/RIVALSblox.lua"))()
end

-- Sistema de monitoramento de mudança de jogo
spawn(function()
    while true do
        wait(AutoExecuteSystem.CheckInterval)
        pcall(CheckGameChange)
    end
end)

-- Sistema de detecção de saída do jogo
game:BindToClose(function()
    if Settings.Misc.AutoExecute then
        print("🔄 Jogo fechando... Sistema de auto-execução ativo para próxima sessão.")
    end
end)

print("✅ Sistema de Auto-Execução inicializado!")

print("🎯 RIVALS Blox Hack carregado com sucesso!")
print("📋 Pressione INSERT para abrir/fechar o menu")
print("🖱️ Use o botão direito do mouse para aimbot")
print("✨ ESP: Box, Line, Distance, Health e Name ativados!")
print("🎯 Aimbot: FOV configurável com smoothness!")
