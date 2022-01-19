local game = remodel.readPlaceFile(".remodel/World.rbxl")

local Models = game.Workspace

for _, model in ipairs(Models:GetChildren()) do
	remodel.writeModelFile(model, "workspace/" .. model.Name .. ".rbxmx")
end