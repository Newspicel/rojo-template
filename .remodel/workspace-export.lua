local game = remodel.readPlaceFile(".remodel/World.rbxl")

-- In this example, we have a bunch of models stored in
-- ReplicatedStorage.Models. We want to put them into a folder named models,
-- maybe for a tool like Rojo.
local Models = game.Workspace

for _, model in ipairs(Models:GetChildren()) do
	remodel.writeModelFile(model, "workspace/" .. model.Name .. ".rbxmx")
end

-- And that's it!